from django.contrib import admin
from django.urls import path,include
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', include('firstpage.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('stock/', include('stock.urls')),
]

from django.conf import settings
from django.conf.urls.static import static



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)