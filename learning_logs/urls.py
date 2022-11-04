
from django.urls import path
from . import views

"""Define padrões de URL para learning_logs."""

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:id>/', views.edit_entry, name='edit_entry'),
]
