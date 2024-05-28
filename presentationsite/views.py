# views.py

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Customer, Campaign, Media
from .serializers import CustomerSerializer, CampaignSerializer, MediaSerializer

from .models import EmailModel
from .forms import EmailForm

def home(request):
    return render(request, 'home.html')

def thank_you(request):
    return render(request, 'thank_you.html')

@csrf_exempt
def new_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            new_object = EmailModel.objects.create(email=email)
            return redirect('thank_you')  # Correctly redirect to the 'thank_you' URL name
    else:
        form = EmailForm()
    return render(request, 'home.html', {'form': form})

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class CustomerCampaignsView(generics.ListCreateAPIView):
    serializer_class = CampaignSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return Campaign.objects.filter(customer_id=customer_id)

    def perform_create(self, serializer):
        customer_id = self.kwargs['customer_id']
        customer = Customer.objects.get(id=customer_id)
        serializer.save(customer=customer)

class MediaUploadView(generics.CreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        file = self.request.FILES['media']
        media = Media(media=file, thumbnail_url='', media_url='')
        media.save()
        media.thumbnail_url = self.request.build_absolute_uri(media.media.url)
        media.media_url = self.request.build_absolute_uri(media.media.url)
        media.save()
        serializer.instance = media
