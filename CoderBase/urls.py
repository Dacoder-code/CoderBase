from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home_page'),
    path('register/', views.signup_view, name='signup_page'),
    path('login/', views.login_view, name='login_page'),
    path('logout/', views.logout_view, name='logout_page'),
    path('courses/', views.course, name='course_page'),
    path('about/', views.about, name='about_page'),
#   path('enroll/<int:pk>/', views.enroll, name='enroll_page'),
    # i want to be able to use the int or str function along with the urls
    path('enroll/', views.enroll, name='enroll_page'),
]
