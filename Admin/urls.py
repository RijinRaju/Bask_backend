from . import views
from django.urls import  path,include
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('adm_login',views.admin_login,name="admin_login"),
    path('domains',views.domain,name="domain"),
    path('add_domain',views.add_domain,name="add_domain"),
    path('add_advisors',views.add_advisors,name="add_advisors"),
    path('list_advisors', views.list_advisors, name="list_advisors"),
    path('remove_advisor',views.remove_advisors,name="remove_advisor"),
    path('add_batch',views.add_batch,name="add_batch"),
    path('batch_list',views.batch_list,name="batch_list"),
    path('add_task',views.add_task,name="add_task"),
    path('task_view',views.task_view,name="task_view"),
    
    


]