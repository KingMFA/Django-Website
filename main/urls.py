from django.urls import path
from . import views

urlpatterns = [path("",views.index,name="index"),path("home/",views.home,name="home"),
               path("list/<int:id>", views.list,name="list"), path("create/", views.create,name="create"),
               path("newApp/",views.addSubject,name="newApp"),
              path("list/<int:person>/delete/<int:task_id>",views.removeTask,name="removeTask"),
               ]