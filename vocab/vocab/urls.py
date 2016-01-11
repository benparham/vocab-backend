from django.conf.urls import include, url, patterns
from django.contrib import admin
admin.autodiscover()
from rest_framework.routers import DefaultRouter
from token_login.views import TokenLogin
from vocab.views import UserViewSet
from entries.views import EntryViewSet

from vocab.routers import NoListRouter

router = DefaultRouter()
# router.register(r'users', UserViewSet, base_name='users')
router.register(r'entries', EntryViewSet, base_name='entries')

noListRouter = NoListRouter()
noListRouter.register(r'user', UserViewSet, base_name='user')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(noListRouter.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^token/', TokenLogin.as_view()),
]
