from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.views.generic import TemplateView #для статических страничек сайта
from django.views.i18n import set_language #перевод язывов

app_name = 'hands'

urlpatterns = [
    path('', views.index, name="index"),
    path('about-ruki-milosty-team/', TemplateView.as_view(template_name="app/pages/about.html"), name="about"),#about
    path('all-news-ruki-milosty/', views.NewsListView.as_view(template_name="app/pages/news.html"), name="news"), #news
    path('all-projects-ruki-milosty/', views.ProjectsListView.as_view(), name="projects"), #projects
    path('contacti-ta-partneri/', TemplateView.as_view(template_name="app/pages/contact.html"), name="contact"), #contact
    path('project-detail/<slug:slug>/', views.ProjectDetailView.as_view(), name="projects-detail"),#detail
    path('news-detail/<slug:slug>/', views.NewsDetailView.as_view(), name="news-detail"),#detail
    path('setlang/', set_language, name='set_language'),#перевод язывов
    path('test/', views.test, name="test"), #test-page
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)