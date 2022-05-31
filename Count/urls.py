from django.urls import path
from . import views
urlpatterns = [
    path('views/Count/',views.Count,name="Count")

]