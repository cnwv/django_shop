from django.urls import path
from adminapp import views as admin

app_name = 'adminapp'

urlpatterns = [
    path('', admin.index, name='index'),
    path('admin-users-read/', admin.admin_users_read, name='admin_users_read'),
    path('admin-users-create/', admin.admin_users_create, name='admin_users_create'),
    path('admin-users-update/<int:id>/', admin.admin_users_update, name='admin_users_update'),
    path('admin-users-delete/<int:id>/', admin.admin_users_delete, name='admin_users_delete'),
]
