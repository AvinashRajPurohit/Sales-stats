"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from sales_app.views import index
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


schema_view = get_schema_view(
    openapi.Info(
        title="Sales Management System",
        default_version='v2',
        description="This application handles operations of SMS",
        contact=openapi.Contact(email="deepakrajpurohit945@gmail.com"),
        license=openapi.License(name="Test License"),
    ),
    url='https://myapp963635.herokuapp.com/',
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api/v1/', include('users.urls')),

    path('docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),

    path('api/api.json/', schema_view.without_ui(cache_timeout=0),
         name='schema-swagger-ui-download'),

    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),

    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': 'static'})

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                 document_root=settings.STATIC_ROOT)
