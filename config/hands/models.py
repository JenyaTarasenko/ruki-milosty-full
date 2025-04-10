
from django.db import models
from django.utils.text import slugify 
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Project(models.Model):
    
    STATUS_CHOICES = [
        ('open', _('Відкритий')),
        ('closed', _('Закритий')),
    ]
    name = models.CharField(max_length=255, verbose_name='Назва проєкту')
    slug = models.SlugField(unique=True, blank=True, max_length=200, verbose_name="Слаг проєкту")
    description = models.TextField(verbose_name='Опис проєкту')
    title = models.TextField(verbose_name='Особливості проєкту')
    main_image = models.ImageField(upload_to='projects/', verbose_name="Головне зображення проєкту")
    project_image1 =  models.ImageField(upload_to='projects/', blank=True, null=True, verbose_name="Зображення перше проєкту")
    project_image2 = models.ImageField(upload_to='projects/', blank=True, null=True, verbose_name="Зображення друге проєкту")
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='open', verbose_name="Статус проєкта")
    created_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата створення проєкту")
    author = models.CharField(max_length=100, verbose_name="Автор статті проєкту")
    partner = models.CharField(max_length=255, blank=True, null=True,  verbose_name="Партнер" )
    
    
 
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Если слаг не задан
            self.slug = slugify(self.name)  # Генерируем слаг на основе имени
        super().save(*args, **kwargs)
        
        
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse("hands:projects-detail", kwargs={"slug": self.slug})
    
    

    
    
class News(models.Model):
        
    name =models.CharField(max_length=255, verbose_name='Назва новини')
    description = models.TextField(verbose_name='Опис новини')
    slug = models.SlugField(unique=True, blank=True, max_length=200, verbose_name="Слаг новини")
    title = models.TextField(verbose_name='Особливості новини')
    main_image = models.ImageField(upload_to='news/', verbose_name="Головне зображення новини")
    news_image1 =  models.ImageField(upload_to='news/', blank=True, null=True, verbose_name="Зображення перше новини")
    news_image2 = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name="Зображення друге новини")
    created_at = models.DateTimeField(null=True, blank=True,verbose_name="Дата створення новини")
    author = models.CharField(max_length=100, verbose_name="Автор статті новини")
    partner = models.CharField(max_length=255, blank=True, null=True,  verbose_name="Партнер" )
    
    
    
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Если слаг не задан
            self.slug = slugify(self.name)  # Генерируем слаг на основе имени
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("hands:news-detail", kwargs={"slug": self.slug})
    
 
    

    
    
