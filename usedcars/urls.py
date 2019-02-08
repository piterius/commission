from django.urls import path
from usedcars import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
    path('', views.api_root),
    path('usedcars/', views.CarList.as_view(), name='car-list'),
    path('usedcars/<int:pk>/', views.CarDetail.as_view(), name='car-detail'),
    path('fields/', views.FieldList.as_view(), name='field-list'),
    path('fields/<int:pk>/', views.FieldDetail.as_view(), name='field-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
