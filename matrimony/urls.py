from django.urls import path
from .views import *

app_name='matrimony'

urlpatterns = [
    path('new_profile/', ProfileCreateView.as_view(), name='new_profile'), #CREATE
    path('', ProfileListView.as_view(), name='profile_list'), #READ
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'), #READ
    path('<int:pk>/update/', ProfileUpdateView.as_view(), name='profile_update'), #UPDATE
    path('<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile_delete'), #DELETE
    path('contact/', ContactView.as_view(), name='contact'),#FORM
    path('example/', ExampleTemplate.as_view(), name='example'),#TEMPLATE
]
