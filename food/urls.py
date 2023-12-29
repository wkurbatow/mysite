from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    # /food/
    path('', views.index, name='index'),
    # /food/str
    path('<int:item_id>/', views.detail, name='detail'),
    path('item/', views.item, name='item'),
    path('add/', views.create_item, name='create_item'),
    

]
