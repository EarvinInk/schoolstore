from . import views
from django.urls import path

app_name = 'schoolstore'

urlpatterns = [
    path('', views.home, name='home'),
    path('order/', views.place_order.as_view(), name='order'),
    path('ajax/get_courses/', views.get_courses, name='ajax_get_courses'),
    path('sucess/',views.sucess,name='sucess')

]
