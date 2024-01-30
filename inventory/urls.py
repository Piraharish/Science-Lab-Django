from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register_invo/',views.register_invo, name='register_invo'),
    path('login_invo/', views.login_invo, name='login_invo'),
    path('home_invo/',views.home_invo, name='home_invo'),
    path('view_distributor/', views.view_distributor, name='view_distributor'),
    path('view_report1/', views.view_report1),
    path('view_report2/', views.view_report2),
    path('view_report3/', views.view_report3),
    path('view_report4/', views.view_report4),
    path('view_report5/', views.view_report5),
    path('inventory_registration/', views.inventory_registration),
    path('admin_to_inventory/', views.admin_to_inventory),
    path('send_to_packing1/<int:id>/', views.send_to_packing1),
    path('send_to_packing2/<int:id>/', views.send_to_packing2),
    path('send_to_packing3/<int:id>/', views.send_to_packing3),
    path('send_to_packing4/<int:id>/', views.send_to_packing4),
    path('send_to_packing5/<int:id>/', views.send_to_packing5),
    path('send1_to_distributor/', views.send1_to_distributor),
    path('send2_to_distributor/', views.send2_to_distributor),
    path('send3_to_distributor/', views.send3_to_distributor),
    path('send4_to_distributor/', views.send4_to_distributor),
    path('send5_to_distributor/', views.send5_to_distributor),
    path('view_distributor1/<int:id>/',views.view_distributor1),
    path('view_distributor2/<int:id>/', views.view_distributor2),
    path('view_distributor3/<int:id>/', views.view_distributor3),
    path('view_distributor4/<int:id>/', views.view_distributor4),
    path('view_distributor5/<int:id>/', views.view_distributor5),


    path('invo_logout/', views.invo_logout, name='invo_logout')
    ]