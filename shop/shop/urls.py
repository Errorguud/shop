from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from anime.views import index_anime
from anime_info.views import info_anime
from shop_index.views import shop_andex_one

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_anime),
    path('info/', info_anime),
    path('shop/', shop_andex_one),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
