from django.urls import path,include
from . import views
from Yongqi import testdb

urlpatterns = [
    path('Read/',views.Read,name="Read"),
    path('testdb/', testdb.testdb)


]