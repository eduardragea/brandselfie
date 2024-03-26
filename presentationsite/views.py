# views.py

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

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
