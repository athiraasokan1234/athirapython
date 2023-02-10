
from django.urls import path,include
from  .import views
app_name='cinemaapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    #path('add/',views.add_cinema,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('add/', views.add, name='add')

]

