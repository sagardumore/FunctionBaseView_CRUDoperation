from django.urls import path
from .import views

urlpatterns=[
    path('addlaptop/',views.AddLaptopView,name='add_laptop'),
    path('showlaptop/',views.ShowLaptopView,name='show_laptop'),
    path('delete/<int:i>/',views.deleteLaptopView,name='delete_laptop'),
    path('update/<int:i>/', views.updateLaptopView, name='update_laptop')

]