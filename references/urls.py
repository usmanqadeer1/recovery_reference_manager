from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reference/<int:reference_id>/', views.reference_detail, name='reference_detail'),
    path('add-reference/', views.add_reference, name='add_reference'),
    path('reference/<int:reference_id>/add-media/', views.add_media, name='add_media'),
    path('reference/<int:reference_id>/edit/', views.edit_reference, name='edit_reference'),
    path('import-excel/', views.import_excel, name='import_excel'),
    path('download-template/', views.download_template, name='download_template'),
]
