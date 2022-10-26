from django.urls import path
from . import views

urlpatterns=[
    #user create login and logout
    path('',views.index,name='index'),
    path('usersignup',views.usersignup,name='usersignup'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('student',views.student,name='student'),
    
    path('usercreate',views.usercreate,name='usercreate'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('logout',views.logout,name='logout'),
    
    
    
    #student registration
    path("add",views.add,name="add"),
    path("add_product", views.add_product, name="add_product"),
    path("show_products", views.show_products, name="show_products"),
    path("edit_product_details/<int:id>", views.edit_product_details, name="edit_product_details"),
    path('editpage/<int:id>',views.editpage,name='editpage'),
    path("delete/<int:id>",views.delete,name='delete'),
]