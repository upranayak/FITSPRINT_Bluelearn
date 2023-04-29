from django.urls import path
from .views import Login, SignUp, Index,outdoor,Indoor,timing,register,Success,Devices,PayNow
from .views import timing_all,Success_Custom,Logout
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', Index.as_view(), name='indexpage'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('signup', SignUp.as_view(), name='signup'),
    path('outdoor',outdoor.as_view(),name='outdoor'),
    path('Indoor',Indoor.as_view(),name='Indoor'),
    path('timing',timing.as_view(),name='timing'),
    path('timing_all',timing_all.as_view(),name='timing_all'),
    path('register',register.as_view(),name='register'),
    path('success', Success.as_view(), name='success'),
    path('Devices',Devices.as_view(),name='Devices'),
    path('PayNow',PayNow.as_view(),name="PayNow"),
    path('success_custom', Success_Custom.as_view(), name='success_all'),
]