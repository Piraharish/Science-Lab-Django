from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register_research/',views.register_research, name='register_research'),
    path('login_research/', views.login_research, name='login_research'),
    path('home_research/',views.home_research, name='home_research'),
    path('registration/', views.registration),
    path('report1/', views.report1),
    path('report2/', views.report2),
    path('report3/', views.report3),
    path('report4/', views.report4),
    path('report5/', views.report5),
    path('view_admin_research/', views.view_admin_research),
    path('send_invo1/',views.send_invo1),
    path('send_invo2/',views.send_invo2),
    path('send_invo3/',views.send_invo3),
    path('send_invo4/', views.send_invo4),
    path('send_invo5/', views.send_invo5),
    path('view_invo1/<int:id>/',views.view_invo1),
    path('view_invo2/<int:id>/',views.view_invo2),
    path('view_invo3/<int:id>/',views.view_invo3),
    path('view_invo4/<int:id>/', views.view_invo4),
    path('view_invo5/<int:id>/',views.view_invo5),

    path('research_logout/', views.research_logout, name='research_logout')
    ]
