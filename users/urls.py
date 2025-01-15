from django.urls import path
from .views import UserLoginView, user_logout, SignUpView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]