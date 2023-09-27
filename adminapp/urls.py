from django.urls import path
from adminapp import views as admin

app_name = 'adminapp'

urlpatterns = [
    path('', admin.index, name='index'),
    path('admin-users-read/', admin.UserListView.as_view(), name='admin_users_read'),
    path('admin-users-create/', admin.UserCreateView.as_view(), name='admin_users_create'),
    path('admin-users-update/<int:pk>/', admin.UserUpdateView.as_view(), name='admin_users_update'),
    path('admin-users-delete/<int:pk>/', admin.UserDeleteView.as_view(), name='admin_users_delete'),
]
