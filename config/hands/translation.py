from modeltranslation.translator import register, TranslationOptions
from .models import Project, News


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'title', 'author', 'partner')

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'title',  'author', 'partner')