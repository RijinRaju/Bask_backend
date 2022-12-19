from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenRefreshView)
from .views import MyTokenObtainPairView
urlpatterns = [
    path('api/token', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup',views.signUp,name="signup"),
    path('login',views.login,name="login"),
    path('profile',views.profile,name="profile"),
    
]
