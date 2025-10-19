from django.urls import path
from .views import ThreadDetail, ThreadList, add_message, newThread


messenger_patterns = ([
    path('', ThreadList.as_view(), name='threads_list'),
    path('thread/<int:pk>/', ThreadDetail.as_view(), name='thread_detail'),
    path('thread/<int:pk>/msg/', add_message, name='add_msg'),
    path('thread/new-msg/<username>/', newThread, name='new_msg'),

]), 'messenger'
