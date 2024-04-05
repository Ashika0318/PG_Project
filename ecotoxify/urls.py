
from django.urls import path
from .import views
urlpatterns = [
    path('ecotoxify_RL/',views.ecotoxify_RL),
    path('ecotoxify_login/',views.ecotoxify_login),
    path('ecotoxify_logout/',views.ecotoxify_logout),
    path('ecotoxify_home/',views.ecotoxify_home),
    path('f_report/',views.f_report),
    path('process_ecotoxify/',views.process_ecotoxify),
    path('analysis_ecotoxify/<str:s_id>/',views.analysis_ecotoxify),
    path('ecotoxify_report/',views.ecotoxify_report)
]
