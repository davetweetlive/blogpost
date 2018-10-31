from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_login_signup, name = 'index_login_signup_function'),
    path('home/', views.welcome_home, name = 'login_function'),
    path('logout/', views.visit_again, name = 'logout_function'),
    path('post/',views.post_blog, name = 'blog_post_function'),
]
