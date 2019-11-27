from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views.generic import View, ListView, DetailView
from .models import Air

# Create your views here.


def Home_View(request):
    if request.user.is_authenticated:
        user_name = request.user
    return  render(request, 'core/index.html', {'user': user_name})

class AirDetail(DetailView):
    model = Air
    template_name = 'core/air_detail.html'

class AirList(ListView):
    model = Air

def About_View(request):
    return render(request, 'core/about.html', {})


class SearchList(View):
    def get(self, request):
        try:
            query = request.GET.get('q')
            print(query)
            air_list = Air.objects.filter(location__icontains=query, description__icontains=query)
            template_name = 'core/search_list.html'
            return render(request, template_name, {'airs': air_list})
        except:
            template_name = 'core/index.html'
            return render(request, template_name, {})
        
