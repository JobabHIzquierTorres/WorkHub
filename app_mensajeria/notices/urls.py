from django.urls import path
from .views import NoticeCreate, NoticeDetailView, NoticeListView, NoticeUpdate, NoticeDelete


notices_patterns = ([
    # lista noticias
    path('', NoticeListView.as_view(), name='notices'),
    # noticia
    path('<int:pk>/<slug:slug>/', NoticeDetailView.as_view(), name='notice'),
    # crea noticia nueva
    path('create/', NoticeCreate.as_view(), name='create'),
    # actualiza noticia
    path('update/<int:pk>', NoticeUpdate.as_view(), name='update'),
    path('delete/<int:pk>', NoticeDelete.as_view(), name='delete'),

]), 'notices'
