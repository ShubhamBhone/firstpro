from django.urls import path
from todoapp import views
urlpatterns = [
    path('home/', views.home),
    path('add/', views.add),
    path('delete/<int:stuid>/',views.delete),

]
