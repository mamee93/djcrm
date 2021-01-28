from django.urls import path
from . import views
app_name= 'leads'
urlpatterns = [
     path('', views.LeadListView.as_view(),name="lead-list"),
     path('<int:pk>/', views.LeadDetail.as_view(),name="lead-detail"),
     
     path('<int:pk>/update/', views.UpdateLeadView.as_view(),name="lead-update"),
     path('<int:pk>/delete/', views.DeleteLeadView.as_view(),name="lead-delete"),
     path('create/', views.CreateLeadView.as_view(),name="lead-create"),
]