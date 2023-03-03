from unicodedata import name
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenRefreshView)
from .views import MyTokenObtainPairView
urlpatterns = [
    # path("notification/<str:room_name>/", views.room, name="room"),
    path('api/token', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup',views.signUp,name="signup"),
    path('login',views.login,name="login"),
    path('profile',views.profile,name="profile"),
    path('task_view',views.task_view,name="task_view"),
    path('del_tsk',views.del_task,name="del_tsk"),
    path('domains',views.domains,name="domains"),
    path('prf_update',views.profile_update,name="profile update"),
    path('sub_answers',views.submit_answers,name="sub answers"),
    path('adv_list',views.advisor_list,name="advisors list"),
    path("address",views.add_address,name="add address"),
        path("fch_add",views.fetch_address,name="fetch address"),
    
]
