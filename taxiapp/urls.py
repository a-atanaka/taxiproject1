#from django.contrib import admin
from django.urls import path
from .views import signupfunc,loginfunc,listfunc,logoutfunc,detailfunc,TaxiCreate,TaxiDelete,TaxiUpdate

urlpatterns = [
    path('signup/', signupfunc,name='signup'),
    path('login/', loginfunc,name='login'),
    path('list/', listfunc, name='list'),
    path('logout/',logoutfunc,name='logout'),
    path('detail/<int:pk>',detailfunc,name='detail'),
    path('create/',TaxiCreate.as_view(),name='create'),
    path('delete/<int:pk>',TaxiDelete.as_view(),name='delete'),
    path('update/<int:pk>',TaxiUpdate.as_view(), name='update'),
]
