from django.urls import path
from . import views

urlpatterns = [   
    path('create/',views.create_rval, name='create'),
    path('update/',views.update_rval, name='update'),
    path('delete/',views.delete_rval, name='delete'),
    path('',views.index, name='index'),
]