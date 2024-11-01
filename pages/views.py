from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user = self.request.user
            context['favorites'] = user.favorites.all()
        else:
            context['favorites'] = []
        return context

class AboutusPageView(TemplateView):
    template_name = 'pages/aboutus.html'

class WishListView(TemplateView):
    template_name = 'pages/wishlist.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user = self.request.user
            context['favorites'] = user.favorites.all()
        else:
            context['favorites'] = []
        return context