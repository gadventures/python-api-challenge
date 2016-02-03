from django.views.generic import TemplateView


class TripView(TemplateView):
    template_name = 'trips/index.html'
