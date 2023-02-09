from src.administration.admins.models import Package
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['packages'] = Package.objects.all()
        return context


class PrivacyPolicyView(TemplateView):
    template_name = 'website/privacy-policy.html'


class TermsAndConditionsView(TemplateView):
    template_name = 'website/terms-and-conditions.html'

