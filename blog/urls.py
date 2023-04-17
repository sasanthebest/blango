from django.urls import path
from . import views
urlpatterns=[
  path(r'',views.index),
  path(r'post/<str:slug>/',views.post_detail,name="blog-post-detail")
]