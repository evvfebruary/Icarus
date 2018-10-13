from django.conf.urls import url, include

from rest_framework import routers
from IcarusDP.views import CampaignView


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^dpcheck', CampaignView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
