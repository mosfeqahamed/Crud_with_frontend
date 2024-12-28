"""
URL configuration for djangorest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from drapi import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('teachers/', views.get_all_teachers, name='get_all_teachers'),  # GET all teachers
    path('teachers/<int:pk>/', views.get_all_teachers, name='get_teacher_by_id'),  # GET a teacher by ID
    path('teachers/create/', views.create_teacher, name='create_teacher'),  # POST to create a new teacher
    path('teachers/update/<int:pk>/', views.update_teacher, name='update_teacher'),  # PUT to update a teacher
    path('teachers/delete/<int:pk>/', views.teacher_detail_or_delete, name='delete_teacher'),  # DELETE to delete a teacher
]
