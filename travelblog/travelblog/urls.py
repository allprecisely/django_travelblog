from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import include
from django.urls import path
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('captcha/', include('captcha.urls')),
    path('', include('main.urls')),
]

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
