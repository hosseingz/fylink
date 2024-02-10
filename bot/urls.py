from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'bot'

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='index'),
    path('login/', auth_views.LogoutView.as_view(), name='index'),

    path('logout/', views.index, name='index'),
    # path('admin-panel/', views.admin_panel, name='admin_panel'),

    # Models
    # path('admin-panel/BotUser/', views.index, name='index'),
    # path('admin-panel/Referra/', views.index, name='index'),
    # path('admin-panel/Subscription/', views.index, name='index'),
    # path('admin-panel/Address/', views.index, name='index'),
    # path('admin-panel/Transaction/', views.index, name='index'),
    # path('admin-panel/Hard/', views.index, name='index'),
    # path('admin-panel/Report/DailyReport', views.index, name='index'),
    # path('admin-panel/Report/MonthlyReport', views.index, name='index'),

    # Commends from bot to server
    path('Commends/new-user/', views.new_user, name='new_user'),



    # path('Commends/referral/', views.new_user, name='new_user'),
    # path('Commends/Subscription/', views.new_user, name='new_user'),
    # path('Commends/Address/', views.new_user, name='new_user'),
    # path('Commends/Transaction/', views.new_user, name='new_user'),
    # path('Commends/Hard/', views.new_user, name='new_user'),
    # path('Commends/DailyReport/', views.new_user, name='new_user'),
    # path('Commends/MonthlyReport/', views.new_user, name='new_user'),

]