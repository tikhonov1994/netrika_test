from django.urls import path

from cities import views

app_name = 'cities'

urlpatterns = [
    path('', views.CityView.as_view(), name='index'),
    path('<str:city>/', views.CitizenView.as_view(), name='city'),
]
