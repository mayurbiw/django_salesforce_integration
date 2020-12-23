from django.urls import path
from . import views

urlpatterns = [
    path("list_accoounts",views.list_accounts,name="list_accounts"),
    path("",views.index,name="index"),
    path("add_account",views.add_account,name="add_account"),
]