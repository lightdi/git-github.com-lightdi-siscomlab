from django.urls import path
from .views import index, laboratorio, informar_problema
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('laboratorio/<int:id>/', laboratorio, name='laboratorio'),
    path('informar_problema/<int:id>/', informar_problema, name='informar_problema'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    
]