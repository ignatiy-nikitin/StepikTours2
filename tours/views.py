from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request):
        return render(request, 'tours/index.html')


class DepartureView(View):
    def get(self, request, departure):
        return render(request, 'tours/departure.html')


class TourView(View):
    def get(self, request, id):
        return render(request, 'tours/tour.html')


def custom_handler_404(request, exception):
    return render(request, 'tours/error_404.html')


def custom_handler_500(request):
    return render(request, 'tours/error_500.html')
