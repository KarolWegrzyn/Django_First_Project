from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from django.urls import path
from komiksyweb.views import login_view, logout_view
from rest_framework import routers
from komiksyweb.views import UserView

router = routers.DefaultRouter()
router.register(r'users', UserView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('komiksy/', include('komiksyweb.urls')), #dodanie wszystkich url z pliku komiksyweb -> urls
    path('login/', login_view, name='login_url'),
    path('logout/', logout_view, name='logout_url'),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



