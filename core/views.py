from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views.generic import View, ListView, DetailView
from .models import Air

# Create your views here.


def Home_View(request):
    if request.user.is_authenticated:
        user_name = request.user
    return  render(request, 'core/index.html', {'user': user_name})

class Air_Detail(DetailView):
    model = Air
    template_name = 'core/air_detail.html'

def About_View(request):
    return render(request, 'core/about.html', {})

def Search(request):
    pass

# class SearchList(ListView):
#     query = request.GET.get('q')
#     queryset = Air.objects.filter(title__icontains = query, description__icontains = query)

#     if query:
#         template_name = 'core/search_list.html'
#     else:
#         template_name = 'core/index.html'
#     # model = Air
#     # template_name = 'core/search_list.html'
    
#     def meta(self, request):
#         try:
#             query = request.GET.get('q')
#             print(query)
#             airs = Air.objects.filter(title__icontains = query, description__icontains = query)
#             template_name = 'core/search_list.html'
#             return render(request, 'core/search_list.html', {})
#         except:
#             template_name = 'core/index.html'
#             return render(request, 'core/index.html', {})


class SearchList(View):
    def get(self, request):
        try:
            query = request.GET.get('q')
            print(query)
            air_list = Air.objects.filter(title__icontains=query, description__icontains=query)
            template_name = 'core/search_list.html'
            return render(request, template_name, {'airs': air_list})
        except:
            template_name = 'core/index.html'
            return render(request, template_name, {})
        
# this works
# def SearchList(request):
#         try:
#             query = request.GET.get('q')
#             print(query)
#             airs = Air.objects.filter(title__icontains = query, description__icontains = query)
#             return render(request, 'core/search_list.html'), {}
#         except:
#             return render(request, 'core/index.html', {})
