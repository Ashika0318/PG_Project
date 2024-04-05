
from django.urls import path
from .import views
urlpatterns = [
    path('commencify_RL/', views.commencify_RL),
    path('commencify_login/',views.commencify_login),
    path('commencify_logout/',views.commencify_logout),
    path('commencify_home/',views.commencify_home),
    path('explore_req/', views.explore_req),
    path('process_req/',views.process_req),
    path('cresultprocess/<str:s_id>/', views.cresultprocess),
    path('c_result/', views.c_result)
]
