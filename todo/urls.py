from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, \
    CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.index, name="index"),
    # path("task/", views.taskList, name="tasks"),
    path("task_list/", TaskList.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task"),
    path("task_create/", TaskCreate.as_view(), name="task_create"),
    path("task_update/<int:pk>/", TaskUpdate.as_view(), name="task_update"),
    path("task_delete/<int:pk>/", DeleteView.as_view(), name="task_delete"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),

]
