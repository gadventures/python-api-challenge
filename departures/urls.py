from django.conf.urls import url

from .views import DepartureView

urlpatterns = [
    url('^', DepartureView.as_view())
]
