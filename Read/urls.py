from django.urls import path
from . import views
from Yongqi import testdb

urlpatterns = [
    path('views/Read/',views.Read,name="Read"),
    path('testdb/', testdb.testdb)


]