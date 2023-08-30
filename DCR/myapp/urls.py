from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index_view, name='myapp_index'),
    path('result/<str:task_id>/', views.check_result_view, name='check_result'),
]