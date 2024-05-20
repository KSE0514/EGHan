from django.urls import path, include
from . import views 
from .views import UpdateProfileView
app_name = 'accounts'
urlpatterns = [
    path('signup/', views.CustomRegisterView.as_view(), name='signup'),
    path('', include('dj_rest_auth.urls')),
    # path('logout/', views.logout, name = 'logout'),
    path('userinfo/',views.user_info,name="user_info"),
    path('update/', UpdateProfileView.as_view(), name = 'update'),
]