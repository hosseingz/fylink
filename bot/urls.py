from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'bot'

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='index'),
    path('login/', auth_views.LogoutView.as_view(), name='index'),

    path('logout/', views.index, name='index'),
    # path('admin-panel/', views.admin_panel, name='admin_panel'),


    # API
    path('Commends/new-user/', views.new_user, name='new_user'),
    path('Commends/user-info/', views.user_info, name='user_info'),
    path('Commends/files/', views.get_files, name='is_linked'),
    path('Commends/download-list/', views.download_list, name='download_list'),
    path('Commends/has-attr/', views.check_Subscription, name='check_Subscription'),
    path('Commends/add-to-download-list/', views.add_download_list, name='add_download_list'),


]