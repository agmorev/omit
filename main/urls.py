from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import MainView, PortfolioDetailsView, ServiceDetailsView
from django.views.generic import TemplateView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('portfolio-details/<int:pk>/', PortfolioDetailsView.as_view(), name='portfolio_details'),
    path('service-details/<int:pk>/', ServiceDetailsView.as_view(), name='service_details'),
    #path('protfolio-details/<int:pk>', TemplateView.as_view(template_name='main/portfolio-details.html'), name='portfolio_details')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)