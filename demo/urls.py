from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view
from .swagger_schema import SwaggerSchemaView

schema_view = get_swagger_view(title='Demo Swagger API')

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^cbv/', include('cbv_demo.urls')),
    url(r'^fbv/', include('fbv_demo.urls')),
    url(r'^swagger/', SwaggerSchemaView.as_view()),


]