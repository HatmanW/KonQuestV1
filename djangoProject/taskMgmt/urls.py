#urls.py
"""
URL configuration for taskMgmt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
import taskMgmt

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),  # URL for adding a new task
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),  # URL for editing an existing task
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # URL for deleting a task
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),  # URL for task details
    path('complete/<int:task_id>/', views.mark_complete, name='mark_complete'),  # URL for marking a task as complete

    #Authentication URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),  # URL for login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL for logout

    # Registration View
    path('register/', views.register, name='register'),

    # Profile paths
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),


    # Password Reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #Admin URL
    path('admin/', admin.site.urls),  # Admin URL
]
