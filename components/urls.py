from django.urls import path
from .import views
app_name = 'components'

urlpatterns = [
     path('', views.index, name='index'),
     path('announcement/', views.announcement, name='announcement'),
     path('new_announ', views.new_announ, name='new_announ'),
     path('edit_announ/<int:announcement_id>/', views.edit_announ, name='edit_announ'),
     path('delete_announ/<int:announcement_id>/', views.delete_announ, name='delete_announ')
]