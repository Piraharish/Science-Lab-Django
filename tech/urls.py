from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tech_admin/',views.tech_admin, name='tech_admin'),
    path('admin_home/',views.admin_home, name='admin_home'),
    path('approve_distributor/',views.approve_distributor, name='approve_distributor'),
    path('approve_true/<int:id>/', views.approve_true, name='approve_true'),
    path('approve_research/',views.approve_research),
    path('send_research/<int:id>/', views.send_research),
    path('inventory_approve/',views.inventory_approve),
    path('send_inventory/<int:id>/',views.send_inventory),
    path('admin_logout/', views.admin_logout, name='admin_logout')

    ]