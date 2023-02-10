from django.http import FileResponse, Http404

from src.administration.admins.models import Package, ApplicationSoftware
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['packages'] = Package.objects.all()
        app = ApplicationSoftware.objects.all().order_by('-version')
        context['app'] = app[0] if app else None
        return context


class PrivacyPolicyView(TemplateView):
    template_name = 'website/privacy-policy.html'


class TermsAndConditionsView(TemplateView):
    template_name = 'website/terms-and-conditions.html'


def download_app(request):

    # CHECK: if requested version is available or not
    app = ApplicationSoftware.objects.filter().order_by('-version')

    if app:

        # STATISTICS: update statistics
        app = app[0]
        app.total_downloads += 1
        app.save()

        # SAVE: download settings
        file = app.app_file
        file_extension = str(file).split('.')[1]
        file_name = f"{app.name} - {app.version}.{file_extension}"
        response = FileResponse(file)
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'

        return response
    raise Http404
