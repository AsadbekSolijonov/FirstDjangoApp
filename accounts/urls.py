from django.urls import path
from accounts import views as account_view
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('register/', account_view.register, name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/', account_view.profile, name='profile'),
    path('change_profile/', account_view.change_profile, name='change_profile'),

]
