from django.urls import path
from . import views

urlpatterns = [
    

    path('std_mnfst',views.students_manifest,name="students manifest"),
    path('manifest',views.manifest,name="manifest"),
    path('upd_mnfst',views.update_manifest,name="update manifest"),
    path('chat_list',views.chat_list,name="chat list"),
    path('chat_record',views.chat_record,name="chat record"),
    path('adv_batchlst',views.advisor_batch_list,name="batch list"),
    path('add_report',views.batch_report,name="add report"),
    path('list_reports',views.list_reports,name="list reports"),
    path('chk_task',views.check_task,name="check task"),
    path('task_verify',views.verify_task,name="task verify")

]
