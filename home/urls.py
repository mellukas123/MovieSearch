from django.contrib import admin
from django.urls import path, include
from home.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include('search.urls')),  # Include app-specific URLs
    path('', home_view, name='home'),
]
