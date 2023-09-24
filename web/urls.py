from django.urls import path

from . import views

urlpatterns = [
    path('', views.days_list,name='days_list'),
    path('<int:day>', views.dynamic_days_by_number),
    path('date_time', views.date_time, name = 'times-of-today'),
    path('<str:day>',views.dynamic_day, name = 'days-of-week'),
]
