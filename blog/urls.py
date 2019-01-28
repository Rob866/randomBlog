from django.urls import path
from . import views

app_name= 'blog'

urlpatterns = [
    
    path('',views.about_page,name="about_page"),
    path('lista/',views.post_list,name="post_list"),
    path("lista/tag/<slug:tag_slug>",views.post_list,name="post_list_by_tag"),
    #path('',views.PostListView.as_view(),name='post_list'),
    path('lista/<int:year>/<int:month>/<int:day>/<slug:slug_title>/',views.post_detail,name="post_detail"),
    path('lista/<int:post_id>/share/', views.post_share, name='post_share'),
    path('search/',views.post_search,name='post_search')
   
]
