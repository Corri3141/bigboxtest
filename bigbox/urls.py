from django.contrib import admin
from django.urls import path, include
from .views import BoxListView, ActivityListView, ActivityDetailView, BoxDetailView

urlpatterns = [
    path('box/', BoxListView.as_view(), name="box-list"),
    path('box/<int:pk>/', BoxDetailView.as_view(), name="box-detail"),
    path('box/<int:box_pk>/activity/', ActivityListView.as_view(), name="activities"),
    path('box/<int:box_pk>/activity/<int:pk>', ActivityDetailView.as_view(), name="activity"),
    path('box/<str:slug>/', BoxDetailView.as_view(), name="box-detail"),
]
