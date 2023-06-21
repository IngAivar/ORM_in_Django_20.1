from django.urls import path

from user.apps import UserConfig

app_name = UserConfig.name

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('confirm-email/<str:uidb64>/<str:token>/', EmailConfirmationView.as_view(), name='confirm_email'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='profile'),
    path('profile/update/', UserUpdateView.as_view(), name='profile_update'),
    path('password-reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
]
