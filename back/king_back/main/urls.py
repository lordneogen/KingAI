
from django.contrib import admin
from django.urls import path

from . import views, view_card

urlpatterns = [
    path('cards/', view_card.LIST_Cards.as_view()),
    path('cards/<int:id>/', view_card.LIST_Cards.as_view()),
    path('models/', views.LIST_Num_edu.as_view()),
    path('models/<int:id>/', views.LIST_Num_edu.as_view()),
    path('kings/', views.LIST_Trys.as_view()),
    path('kings/<int:id>/', views.LIST_Trys.as_view()),
]
