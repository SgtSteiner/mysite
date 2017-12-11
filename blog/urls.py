# from django.conf.urls import url
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # post views
    # url(r'^$', views.post_list, name="post_list"),
    path('',
         views.PostListView.as_view(),
         name="post_list"),
    path('<int:year>/<int:month>/<int:day>/<post>/',
         views.post_detail,
         name="post_detail")
]
