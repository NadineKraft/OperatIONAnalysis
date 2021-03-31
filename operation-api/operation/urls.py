from django.urls import path
from . import views


urlpatterns = [
    path('experiments/', views.ExperimentList.as_view()),
    path('experiments/<int:pk>/', views.ExperimentDetail.as_view()),
    path('experiments/runprocessing/<int:pk>/', views.ExperimentDetail.as_view()),
    path('configs/', views.ConfigList.as_view()),
    path('configs/<int:pk>/', views.ConfigDetail.as_view()),
    path('analysis/', views.AnalysisList.as_view()),
    path('analysis/runanalysis/<int:pk>/', views.AnalysisDetail.as_view()),
    path('analysis/<int:pk>/', views.AnalysisDetail.as_view()),
]
