from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'website/index.html'


class PrivacyPolicyView(TemplateView):
    template_name = 'website/privacy-policy.html'


class TermsAndConditionsView(TemplateView):
    template_name = 'website/terms-and-conditions.html'

