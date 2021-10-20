from django.conf import settings

from django.contrib import admin

from .main_router import urlpatterns as main
from .yasg_router import urlpatterns as yasg


urlpatterns = main + yasg

admin.site.site_header = "Custom Admin"
admin.site.site_title = "Custom Admin"
admin.site.index_title = "Welcome to Custom Admin Panel"

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
