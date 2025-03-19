from django.contrib import admin
from .models import Project,News


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at', 'main_image','author')
    search_fields = ['name', 'author', 'created_at']
    list_filter = ('status', 'author')
    ordering = ('-created_at',)
    prepopulated_fields = {'slug': ('name',)}
   
    

    


class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'author')
    search_fields = ['name', 'author', 'created_at']
    list_filter = ('author',)
    ordering = ('-created_at',)
    prepopulated_fields = {'slug': ('name',)}
    
  
      
admin.site.register(Project, ProjectAdmin)
admin.site.register(News, NewsAdmin)



