"""
URL configuration for Doctor_Scheduler project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Main.urls')),
    #path('about',),
    path('roster',views.roster_page),
    path('block',views.block_page),
    path('block/create',views.create_edit_block,name='create'),
    path('block/edit/<int:pk>',views.create_edit_block,name='edit'),
    path('block/delete/<int:pk>',views.delete_block,name='delete'),
    path('schedule',views.schedule_page),
]

#if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
