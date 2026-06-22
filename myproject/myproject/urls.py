"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from app1 import views
from app1 .admin import *


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentreg/', views.studentreg),
    path('', views.index),
    path('about_us/', views.about_us),
    path('contact_us/', views.contact_us),
    path('show_cars_all/',views.show_cars_all),

    path('carreg/', views.carreg),
    path('adminreg/', views.adminreg),
    path('show_admin/', views.show_admin),
    path('edit_admin_profile/', views.edit_admin_profile),
    path('save_edit_admin_profile/', views.save_edit_admin_profile),
    path('show_user_profile/', views.show_user_profile),
    path('edit_user_profile/', views.edit_user_profile),
    path('save_edit_user_profile/', views.save_edit_user_profile),
    path('edit_user_password/', views.edit_user_password),
    path('save_edit_user_password/', views.save_edit_user_password),
    path('login/', views.login),
    path('logout/', views.logout),
    path('adminhome/', views.adminhome),
    path('author/', views.author),
    path('userreg/', views.userreg),
    path('show_user_reg/', views.show_user_reg),
    path('show_user/', views.show_user),
    path('userhome/', views.userhome),
    path('show_car/', views.show_car),

    path('edit_cars/',views.edit_cars),
    path('save_edit_cars/',views.save_edit_cars),
    path('delete_car/', views.delete_car),
    path('upload_car_photos/', views.upload_car_photos),
    path('add_to_cart/', views.add_to_cart),
    path('show_add_to_car/', views.show_add_to_car),
    path('booknow/',views.booknow),
    path('save_booking/', views.save_booking),
    path('pay/', views.pay),
    path('show_user_history/', views.show_user_history),
    path('delete_cart/', views.delete_cart),
    path('Accept_booking/', views.Accept_booking),
    path('Reject_booking/', views.Reject_booking),
    path('show_all_bookings/', views.show_all_bookings),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

