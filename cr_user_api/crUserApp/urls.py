from django.urls import path
from .views import create_token, UserCreateView, UserListView

urlpatterns = [
    path('api-token/', create_token, name='api-token'),  # Obtain authentication token
    path('user-create/', UserCreateView.as_view(), name='user-create'),
    path('users/list/', UserListView.as_view(), name='user-list'),
]
