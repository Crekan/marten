from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from food.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),

    path('blog/', include('blog.urls')),
    path('food/', include('food.urls')),
    path('user/', include('user.urls')),
    path('about/', include('about.urls')),
    path('contact', include('contact.urls')),

    path('__debug__/', include('debug_toolbar.urls')),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
