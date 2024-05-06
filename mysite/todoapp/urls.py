from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('add/',views.add_todo,name="add-todo"),
    path('update/<int:pk>/', views.update_todo, name='update-todo'),
    path('delete/<int:pk>/',views.delete_todo,name="delete-todo"),
    path('item_delete/<int:pk>/', views.accept_delete_todo, name='delete-item')

]