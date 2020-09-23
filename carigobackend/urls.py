from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('main.urls')),
    path('api/v1/accounts/', include('accounts.urls')),

    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),
            name='account_confirm_email'),  # Generic email confirmation path to bypass email cnfirmation for now

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
