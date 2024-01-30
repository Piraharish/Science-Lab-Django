from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register_distri/',views.register_distri, name='register_distri'),
    path('login_distri/', views.login_distri, name='login_distri'),
    path('home_disrtibution/',views.home_disrtibution, name='home_disrtibution'),
    path('register_form/',views.register_form, name='register_form'),
    path('admin_view_distributor/',views.admin_view_distributor),
    path('view_tablet1/', views.view_tablet1),
    path('view_tablet2/', views.view_tablet2),
    path('view_tablet3/', views.view_tablet3),
    path('view_tablet4/', views.view_tablet4),
    path('view_tablet5/', views.view_tablet5),
    path('dis_logout/', views.dis_logout, name='dis_logout')
    ]