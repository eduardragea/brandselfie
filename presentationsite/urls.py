from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, CampaignViewSet, CustomerCampaignsView, MediaUploadView

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'campaigns', CampaignViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('customers/<int:customer_id>/campaigns/', CustomerCampaignsView.as_view(), name='customer-campaigns'),
    path('media/', MediaUploadView.as_view(), name='media-upload'),
]
