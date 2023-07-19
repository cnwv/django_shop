from django.urls import path
from adminapp import views as admin

app_name = 'adminapp'

urlpatterns = [
    path('', admin.index, name='index'),
    path('admin-users-read/', admin.admin_users_read, name='admin_users_read')
]
