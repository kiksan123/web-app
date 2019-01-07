from django.urls import path
 
from . import views
 
# アプリケーションの名前空間
# https://docs.djangoproject.com/ja/2.0/intro/tutorial03/
app_name = 'photo'
 
urlpatterns = [
    # ex: /
    path('', views.IndexViews.as_view(), name='index'),
    # ex: /post/create/
    path('post/create/', views.CreateViews.as_view(), name='create'),
    # ex: /post/1/
    path('post/<int:pk>/', views.DetailViwes.as_view(), name='detail')
]
