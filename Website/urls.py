from django.urls import path
from .import views
app_name="Website"

urlpatterns=[
    path("",views.home,name="home"),
    path("project/",views.view_project,name="project"),
    path("email/",views.contact,name="email")
]