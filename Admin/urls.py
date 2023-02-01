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
    path('pend_list', views.pend_list,name="pend_list"),
    path('approve_list',views.approve_list,name="approve_list"),
    path('decline',views.decline,name="declined"),
    path('advisor_list',views.advisor_list,name="advisor_list"),
    path('count_students',views.count_students,name="count student"),
    path('allot_number',views.allot_number,name="allot number"),
    path('stud_lst',views.students_lists,name="students lists"),
    path('weeks',views.weeks,name="weeks"),
    path('prf_update',views.profile_update,name="profile updates"),
    path('prf_load',views.profile_view,name="profile view"),
    path('dom_del/<int:id>',views.delete_domain,name="delete domain")
    
    


]