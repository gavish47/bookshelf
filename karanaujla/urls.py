from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/books', views.BookViewSet)

urlpatterns = [
    path('', views.landing, name='landing'), 
    path('', views.landing_page, name='landing'), 
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add-book/', views.add_book, name='add_book'),
]
