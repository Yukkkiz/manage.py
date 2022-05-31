from django.urls import path
from . import views
urlpatterns = [
    path('views/Visualize/',views.Visualize,name="Visualize")

]