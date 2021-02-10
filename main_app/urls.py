from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('workout/', views.workouts_index, name='index'),
    path('workouts/<int:workout_id>/', views.workouts_detail, name='detail'),
    path('workouts/create/', views.WorkoutCreate.as_view(), name='workouts_create'),
    path('workouts/<int:pk>/delete/', views.WorkoutDelete.as_view(), name='delete'),
    path('workouts/<int:pk>/update/', views.WorkoutUpdate.as_view(), name='update'),
]