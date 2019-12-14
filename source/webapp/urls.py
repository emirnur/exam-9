from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import IndexView, PhotoCreateView, PhotoDetailView, PhotoUpdateView, PhotoDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photos/create/', PhotoCreateView.as_view(), name='photo_create'),
    path('product/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('product/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('product/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
