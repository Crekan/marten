from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from food.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('food/', include('food.urls')),
    path('user/', include('user.urls')),

    path('', HomeView.as_view(), name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
