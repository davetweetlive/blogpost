from django.urls import path
from . import views




urlpatterns = [
    path('', views.index_login_signup, name = 'index_login_signup_function'),
    path('home/', views.welcome_home, name = 'login_function'),
    path('logout/', views.visit_again, name = 'logout_function'),
    path('post/', views.post_blog, name = 'blog_post_function'),
    path('profile/', views.view_profile, name = 'view_profile_function'),
    path('post/<int:post_id>', views.expand_post, name = 'expand_post_function')
]
