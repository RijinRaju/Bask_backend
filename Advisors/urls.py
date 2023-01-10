from django.urls import path
from . import views

urlpatterns = [
    

    path('std_mnfst',views.students_manifest,name="students manifest"),
    path('manifest',views.manifest,name="manifest"),
    path('upd_mnfst',views.update_manifest,name="update manifest"),
    path('chat_list',views.chat_list,name="chat list"),
    path('chat_record',views.chat_record,name="chat record")

]
