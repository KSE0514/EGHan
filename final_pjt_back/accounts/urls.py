from django.urls import path, include
from . import views 
app_name = 'accounts'
urlpatterns = [
    path('signup/', views.CustomRegisterView.as_view(), name='signup'),
    path('', include('dj_rest_auth.urls')),
    # path('logout/', views.logout, name = 'logout'),
    path('update/', views.update, name = 'update'),
]