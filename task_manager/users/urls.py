from django.urls import path
from task_manager.users import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('users/', views.UsersView.as_view()),
    path('users/create/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path(
        'users/<int:pk>/update/',
        views.UpdateUserView.as_view(),
        name='update',
    ),
    path(
        'users/<int:pk>/delete/',
        views.DeleteUserView.as_view(),
        name='delete',
    )
]
