from django.urls import path

from . import views

urlpatterns = [
    path('users/',views.UserApiView.as_view(),name='users'),
]
