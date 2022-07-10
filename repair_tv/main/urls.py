from django.urls import path


from .views import index
from .views import about_site_tm
from .views import contact
from .views import price
from .views import sale_tvs, sale_tv
from .views import SignUpView, RegisterDone
from .views import LogIn, LogOut
from .views import profile
from .views import repair_order, order_done


app_name = 'main'
urlpatterns = [
    path('accounts/register_done', RegisterDone.as_view(), name='register_done'),
    path('accounts/register', SignUpView.as_view(), name='register'),
    path('accounts/login', LogIn.as_view(), name='login'),
    path('accounts/logout', LogOut.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('order_done/', order_done, name='order_done'),
    path('repair_order/', repair_order, name='repair_order'),
    path('sale_tvs/<int:pk>/<slug:slug_tv>/', sale_tv, name='sale_tv'),
    path('sale_tvs/', sale_tvs, name='sale_tvs'),
    path('price/', price, name='price'),
    path('contact/', contact, name='contact'),
    path('about_site_tm/', about_site_tm, name='about_site_tm'),
    path('', index, name='index'),
]
