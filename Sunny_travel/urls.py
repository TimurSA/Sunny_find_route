from django.contrib import admin
from django.urls import path, include

from routes.views import home
from Sunny_travel.views import about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', include(('cities.urls', 'cities'))),
    path('trains/', include(('trains.urls', 'trains'))),
    path('', home, name='home'),
    path('about/', about)
]
