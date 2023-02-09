from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core.settings import MEDIA_ROOT, STATIC_ROOT
from src.accounts.views import (
    GoogleLoginView, FacebookLoginView, AppleLoginView
)


def handler404(request, *args, **kwargs):
    return render(request, "404.html")


def handler500(request, *args, **kwargs):
    return render(request, "500.html")


schema_view = get_schema_view(
    openapi.Info(
        title="AI Genie",
        default_version='v1',
        description="Your AI Genie in a Bottle",
        terms_of_service="https://aigenie.exarth.com/terms-and-conditions/",
        contact=openapi.Contact(email="support@exarth.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# CORE URLS
urlpatterns = [

    # SYS URLS > remove in extreme security
    path('admin/', admin.site.urls),

    # API URLS
    path('accounts/', include('allauth.urls')),

    # APPS URLS
    path('', include('src.website.urls', namespace='website')),
    path('api/', include('src.api.urls', namespace='api')),
    path('accounts/', include('src.accounts.urls', namespace='accounts')),
    path('admins/', include('src.administration.admins.urls', namespace='admins')),
]
# UNIVERSAL URLS
urlpatterns += [
    # 404-500-00 PAGES
    path('under-construction/', TemplateView.as_view(template_name='000.html')),
    path('404/', TemplateView.as_view(template_name='404.html')),
    path('500/', TemplateView.as_view(template_name='500.html')),
]

# Rest Auth UI Configuration
urlpatterns += [
    re_path(r'^social-auth/', include('dj_rest_auth.urls')),
    # re_path(r'^social-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('auth/google/', GoogleLoginView.as_view(), name='google-login-view'),
    path('auth/facebook/', FacebookLoginView.as_view(), name='facebook-login-view'),
    path('auth/apple/', AppleLoginView.as_view(), name='apple-login-view'),
    path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
]


from .settings import ENVIRONMENT
if ENVIRONMENT != 'server':
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls"))
    ]
