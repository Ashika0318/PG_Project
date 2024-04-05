
from django.urls import path
from .import views
urlpatterns = [
   path('admin_login/', views.admin_login),
   path('admin_home/', views.admin_home),
   path('admins_logout/',views.admins_logout),
   path('scientist_reg/', views.scientist_reg),
   path('approve/<int:id>/', views.approve),
   path('reject/<int:id>/',views.reject),
   path('commencify_reg/', views.commencify_reg),
   path('grant/<int:id>/', views.grant),
   path('revoke/<int:id>/',views.revoke),
   path('fibroanalysis_reg/', views.fibroanalysis_reg),
   path('accept/<int:id>/', views.accept),
   path('decline/<int:id>/',views.decline),
   path('ecotoxify_reg/', views.ecotoxify_reg),
   path('admit/<int:id>/', views.admit),
   path('deny/<int:id>/',views.deny),
   path('commencify_result/', views.commencify_result),
   path('capprove/<str:s_id>/', views.capprove),
   path('fibroanalysis_result/',views.fibroanalysis_result),
   path('fibroanalysis_result_report/<str:s_id>/',views.fibroanalysis_result_report),
   path('fapprove/<str:s_id>/',views.fapprove),
   path('ecotoxify_result/',views.ecotoxify_result),
   path('eapprove/<str:s_id>/',views.eapprove),
   path('valid_report/',views.valid_report),
   path('view_final_report/<str:s_id>/',views.view_final_report),
   path('finalreportapprove/<str:s_id>/', views.finalreportapprove)
]
