from django.urls import path
from blogging.views import list_view, detail_view, stub_view

urlpatterns = [path('', list_view, name ='blog_index'),
               path('post/<int:post_id>/', stub_view, name="blog_detail")]
