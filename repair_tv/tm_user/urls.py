from django.urls import path

from tm_user.views import RegisterDone
from tm_user.views import UserSignUpView
from tm_user.views import UserSignInView
from tm_user.views import LogOut
from tm_user.views import profile

app_name = 'tm_user'
urlpatterns = [
    path('register_done/', RegisterDone.as_view(), name='register_done'),
    path('register/', UserSignUpView.as_view(), name='register'),
    path('login/', UserSignInView.as_view(), name='login'),
    path('logout/', LogOut.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
]
