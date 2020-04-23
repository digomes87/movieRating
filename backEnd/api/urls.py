from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from api.views import MovieViewSet, RatingViewSet

routers = routers.DefaultRouter()
routers.register('rating', RatingViewSet)
routers.register('movies', MovieViewSet)


urlpatterns = [
    path('', include(routers.urls)),
]