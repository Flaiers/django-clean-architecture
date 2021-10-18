from rest_framework.permissions import AllowAny

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.urls import path


schema_view = get_schema_view(
   openapi.Info(
      title="Fla API",
      default_version='v1',
      description="This is manual for API",
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[AllowAny],
)

urlpatterns = [
   path('swagger<format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
