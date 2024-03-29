from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register_analyse/',views.register_analyse, name='register_analyse'),
    path('login/', views.login, name='login'),
    path('home/',views.home, name='home'),
    path('analyze1/', views.analyze1, name='analyze1'),
    path('analyze2/', views.analyze2, name='analyze2'),
    path('analyze3/', views.analyze3, name='analyze3'),
    path('analyze4/', views.analyze4, name='analyze4'),
    path('analyze5/', views.analyze5, name='analyze5'),
    path('table1/', views.table1),
    path('table2/', views.table2),
    path('table3/', views.table3),
    path('table4/', views.table4),
    path('table5/', views.table5),
    path('send_company/', views.send_company),
    path('move_company/', views.move_company),
    path('get_input1/<int:id>/', views.get_input1,name='get_input1'),
    path('get_input2/<int:id>/', views.get_input2,name='get_input2'),
    path('get_input3/<int:id>/', views.get_input3, name='get_input3'),
    path('get_input4/<int:id>/', views.get_input4, name='get_input4'),
    path('get_input5/<int:id>/', views.get_input5, name='get_input5'),
    path('view_analyze1/', views.view_analyze1),
    path('send_analyze1/<int:id>/', views.send_analyze1),
    path('reject_analyze1/', views.reject_analyze1),
    path('delete_analyze1/<int:id>/', views.delete_analyze1),
    path('view_analyze2/', views.view_analyze2),
    path('send_analyze2/<int:id>/', views.send_analyze2),
    path('reject_analyze2/', views.reject_analyze2),
    path('delete_analyze2/<int:id>/', views.delete_analyze2),
    path('view_analyze3/', views.view_analyze3),
    path('send_analyze3/<int:id>/', views.send_analyze3),
    path('reject_analyze3/', views.reject_analyze3),
    path('delete_analyze3/<int:id>/', views.delete_analyze3),
    path('view_analyze4/', views.view_analyze4),
    path('send_analyze4/<int:id>/', views.send_analyze4),
    path('reject_analyze4/', views.reject_analyze4),
    path('delete_analyze4/<int:id>/', views.delete_analyze4),
    path('view_analyze5/', views.view_analyze5),
    path('send_analyze5/<int:id>/', views.send_analyze5),
    path('reject_analyze5/', views.reject_analyze5),
    path('delete_analyze5/<int:id>/', views.delete_analyze5),
    # path('sent_to_packing', views.sent_to_packing),

    path('logout/', views.logout, name='logout')
    ]