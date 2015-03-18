from django.contrib import admin
from models import Article,Tag
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','stime')



admin.site.register(Article,ArticleAdmin)
admin.site.register(Tag)