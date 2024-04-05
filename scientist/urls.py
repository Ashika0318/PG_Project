
from django.urls import path
from .import views
urlpatterns = [
   path('', views.index),
   path('scientist_RL/', views.scientist_RL),
   path('scientist_login/',views.scientist_login),
   path('scientist_logout/', views.scientist_logout),
   path('scientist_home/', views.scientist_home),
   path('scientist_requirement/', views.scientist_requirement),
   path('checkpoints/', views.checkpoints)
]
