from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('register',views.register),
    path('logout',views.logout),
    path('login',views.login),
    path('show_register_form',views.showRegisterForm),
    path("show_login_form",views.showLoginForm),
    path('validateEmailByAjax',views.validateEmailByAjax,name="validateEmailByAjax"),
    path('validateFirstNameByAjax',views.validateFirstNameByAjax,name="validateFirstNameByAjax"),
    path('validateLastNameByAjax',views.validateLastNameByAjax,name="validateLastNameByAjax"),
    path('validatePasswordByAjax',views.validatePasswordByAjax,name="validatePasswordByAjax"),
    path('show_add_plan_form',views.showAddPlanForm),
    path('add_travel_plan',views.addPlan),
    path('show_travel_form',views.showTravelForm),
    path('join_to_paln/<int:id>',views.joinPlan),
    path('show_info/<int:id>',views.showInfo),

    
]