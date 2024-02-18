from . import views
from django.urls import include, path
from .views import CustomLoginView


urlpatterns = [
    path('', views.index, name='index'),
    # path('login_user/', views.LoginUser.as_view(), name='login'),
    path('recipe/', views.recipe, name='recipe'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
]