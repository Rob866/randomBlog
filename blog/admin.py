from django.contrib import admin
from .models import Post,Comment



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display=("title","slug","author","publish","status","id")
    list_filter =("status","created","publish","author")
    search_fields=('title','body')
    date_hierarchy='publish'
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    ordering =('status','publish',)




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','created','activate')
    list_filter=('activate','created','updated')
    search_fields=('name','email','body')



