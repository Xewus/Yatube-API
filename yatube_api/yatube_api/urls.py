from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from posts.views import home_view

urlpatterns = [
    path('', home_view),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'), name='api'),
    path('redoc/',
         TemplateView.as_view(template_name='redoc.html'),
         name='redoc'),
]
