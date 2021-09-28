from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .api import api

urlpatterns = [
  
    path('', TemplateView.as_view(template_name="base.html"), name="home"),
    path('accounts/', include('apps.accounts.urls')),
    path("api/", api.urls),

    path('admin/', admin.site.urls),
]


admin.autodiscover()
admin.site.enable_nav_sidebar = False
