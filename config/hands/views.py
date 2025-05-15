from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, News
from django.views.generic import ListView, DetailView
import random
from django.utils import translation

from django.shortcuts import render

def custom_404(request, exception):
    print(type(exception)) 
    return render(request, 'app/pages/404.html', status=404)





def index(request):
    latest_project = Project.objects.order_by()[:3]
    latest_new = News.objects.order_by()[:3]    
    return render(request,'app/pages/index.html', {'latest_project':latest_project, 'latest_new':latest_new })


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'app/pages/projects-detail.html'
    context_object_name = 'projects'
    
    
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       project_item = Project.objects.all()
       if project_item.count() >=3:
            context['random_projects'] = random.sample(list(project_item), 3)
       else:
            context['random_projects'] = project_item 
       return context


class ProjectsListView(ListView):
    model = Project
    template_name = "app/pages/projects.html"
    context_object_name = 'projects'
    paginate_by = 3
    
    
    
class NewsDetailView(DetailView):
    model = News
    template_name = 'app/pages/news-detail.html'
    context_object_name = 'news'
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       news_item = News.objects.all()
       if news_item.count() >=4:
            context['news_projects'] = random.sample(list(news_item), 4)
       else:
            context['news_projects'] = news_item 
       return context


class NewsListView(ListView):
    model = News
    template_name = "app/pages/news.html"
    context_object_name = 'news'
    paginate_by = 3