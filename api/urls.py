from django.urls import path
from .views import PostAPIView,PostDetailApiView

urlpatterns = [
    path('', PostAPIView.as_view(), name = 'post_list'),
    path('<int:pk>/', PostDetailApiView.as_view(),name = 'post_detail'),

]