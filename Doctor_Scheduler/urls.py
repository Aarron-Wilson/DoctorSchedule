from django.contrib import admin
from django.urls import path,include
from Main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Main.urls')),
    path('roster',views.roster_page),
    path('block',views.block_page),
    path('block/create',views.create_edit_block,name='create'),
    path('block/edit/<int:pk>',views.create_edit_block,name='edit'),
    path('block/delete/<int:pk>',views.delete_block,name='delete'),
    path('schedule',views.schedule_page),
    path('manage_job_slots/<int:pk>',views.manage_job_slots),
    path('job_slot/create/<int:pk>',views.add_job_slot),
    path('job_slot/delete/<int:pk>',views.delete_job_slot),
]