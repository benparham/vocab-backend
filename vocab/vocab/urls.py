from django.conf.urls import include, url, patterns
from django.contrib import admin
admin.autodiscover()
from rest_framework.routers import DefaultRouter

from vocab.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
