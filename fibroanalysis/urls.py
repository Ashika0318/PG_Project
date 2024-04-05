from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views
urlpatterns = [
    path('fibroanalysis_RL/', views.fibroanalysis_RL),
    path('fibroanalysis_login/', views.fibroanalysis_login),
    path('fibroanalysis_home/', views.fibroanalysis_home),
    path('fibroanalysis_logout/',views.fibroanalysis_logout),
    path('c_report/',views.c_report),
    path('fire_res_analysis/',views.fire_res_analysis),
    path('f_fireresistence/<str:s_id>/',views.f_fireresistence),
    path('fire_res_analysis_report/',views.fire_res_analysis_report),
    path('thermal_insulation_res_analysis/', views.thermal_insulation_res_analysis),
    path('f_thermalinsulation/<str:s_id>/', views.f_thermalinsulation),
    path('thermal_insulation_analysis_report/', views.thermal_insulation_analysis_report),
    path('sound_absorption_res_analysis/', views.sound_absorption_res_analysis),
    path('f_soundabsorption/<str:s_id>/', views.f_soundabsorption),
    path('sound_absorption_analysis_report/',views.sound_absorption_analysis_report)
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings
                      .MEDIA_ROOT)
