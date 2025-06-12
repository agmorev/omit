from email.message import EmailMessage
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, DetailView
from .forms import ContactForm
from .models import (
    EducationItem,
    PortfolioItem,
    PortfolioItemGallery,
    ServiceItem,
    ServiceItemGallery,
    ServiceItemClients
)
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _


class MainView(SuccessMessageMixin, FormView):
    template_name = 'main/main.html'
    form_class = ContactForm
    success_url = '#contact'
    success_message = _('The message was sent successfully')

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['education_items'] = EducationItem.objects.all().order_by("-end_date")
        context['portfolio_items'] = PortfolioItem.objects.all()
        context['service_items'] = ServiceItem.objects.all().order_by("id")
        return context

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class PortfolioDetailsView(SuccessMessageMixin, DetailView):
    model = PortfolioItem
    template_name = 'main/portfolio-details.html'

    def get_context_data(self, **kwargs):
        context = super(PortfolioDetailsView, self).get_context_data(**kwargs)
        context['portfolio_item_gallery'] = PortfolioItemGallery.objects.filter(item_id=self.kwargs['pk'])
        return context


class ServiceDetailsView(SuccessMessageMixin, DetailView):
    model = ServiceItem
    template_name = 'main/service-details.html'

    def get_context_data(self, **kwargs):
        context = super(ServiceDetailsView, self).get_context_data(**kwargs)
        context['service_item_gallery'] = ServiceItemGallery.objects.filter(item_id=self.kwargs['pk'])
        context['service_item_clients'] = ServiceItemClients.objects.filter(item_id=self.kwargs['pk'])
        return context

