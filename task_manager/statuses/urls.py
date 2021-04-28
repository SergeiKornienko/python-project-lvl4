from django.urls import path
from task_manager.statuses import views

urlpatterns = [
    path('statuses/', views.StatusesView.as_view(), name='statuses'),
    path('statuses/create/', views.CreateStatusView.as_view(), name='create_status'),
    path(
        'statuses/<int:pk>/update/',
        views.UpdateUserView.as_view(),
        name='update',
    ),
    # path(
    #     'users/<int:pk>/delete/',
    #     views.DeleteUserView.as_view(),
    #     name='delete',
    # )
]
