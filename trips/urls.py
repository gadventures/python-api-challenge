from django.conf.urls import url

from .views import TripView

urlpatterns = [
    url('^', TripView.as_view())
]
