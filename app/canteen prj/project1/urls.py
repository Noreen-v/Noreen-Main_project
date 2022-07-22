"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path(r'Student_reg/',Student_reg,name='Student_reg'),
    path(r'Canteen_reg/',Canteen_reg,name='Canteen_reg'),
    path(r'getallcanteen/',getallcanteen,name='getallcanteen'),

    path(r'getallstudents/',getallstudents,name='getallstudents'),
    path(r'Update_canteen/',Update_canteen,name='Update_canteen'),
    path(r'Delete_canteen/',Delete_canteen,name='Delete_canteen'),
    path(r'Update_student/',Update_student,name='Update_student'),
    path(r'Delete_student/',Delete_student,name='Delete_student'),
    path(r'CheckLogin/',CheckLogin,name='CheckLogin'),
    path(r'Add_food/',Add_food,name='Add_food'),
    path(r'Canteen_view_food/',Canteen_view_food,name='Canteen_view_food'),
    path(r'Update_food_details/',Update_food_details,name='Update_food_details'),
    path(r'Disable_food/',Disable_food,name='Disable_food'),
    path(r'Delete_food/',Delete_food,name='Delete_food'),
    path(r'Get_canteendetails/',Get_canteendetails,name='Get_canteendetails'),
    path(r'Student_view_food/',Student_view_food,name='Student_view_food'),
    path(r'Food2cart/',Food2cart,name='Food2cart'),
    path(r'Remove_food/',Remove_food,name='Remove_food'),
    path(r'Getmybucket/',Getmybucket,name='Getmybucket'),
    path(r'Confirm_order/',Confirm_order,name='Confirm_order'),
    path(r'Cancel_order/',Cancel_order,name='Cancel_order'),
    path(r'Student_my_orders/',Student_my_orders,name='Student_my_orders'),
    path(r'Get_order/',Get_order,name='Get_order'),
    path(r'Approve_order/',Approve_order,name='Approve_order'),
    path(r'Canteen_my_orders/',Canteen_my_orders,name='Canteen_my_orders'),
    path(r'Student_my_history/',Student_my_history,name='Student_my_history'),
    path(r'Canteen_my_orders_by_date/',Canteen_my_orders_by_date,name='Canteen_my_orders_by_date'),
]
