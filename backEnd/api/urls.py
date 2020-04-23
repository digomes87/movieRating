from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from api.views import MovieViewSet, RatingViewSet, UserViewSet

routers = routers.DefaultRouter()
routers.register('ratings', RatingViewSet)
routers.register('movies', MovieViewSet)
routers.register('users', UserViewSet)


urlpatterns = [
    path('', include(routers.urls)),
]