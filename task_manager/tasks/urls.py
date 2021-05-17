from django.urls import path
from task_manager.tasks import views

urlpatterns = [
    path('statuses/', views.StatusesView.as_view(), name='statuses'),
    path(
        'statuses/create/',
        views.CreateStatusView.as_view(),
        name='create_status',
    ),
    path(
        'statuses/<int:pk>/update/',
        views.UpdateStatusView.as_view(),
        name='update_status',
    ),
    path(
        'statuses/<int:pk>/delete/',
        views.DeleteStatusView.as_view(),
        name='delete_status',
    ),
    path('tasks/', views.TaskView.as_view(), name='tasks'),
    path(
        'tasks/create/',
        views.CreateTaskView.as_view(),
        name='create_task',
    ),
    path(
        'tasks/<int:pk>/update/',
        views.UpdateTaskView.as_view(),
        name='update_task',
    ),
    path(
        'tasks/<int:pk>/delete/',
        views.DeleteTaskView.as_view(),
        name='delete_task',
    )
]
