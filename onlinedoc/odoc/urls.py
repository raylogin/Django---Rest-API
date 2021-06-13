from django.urls import path
from . import views

urlpatterns = [   
    path('editor/',views.createfile, name='createfile'),
    # path(r'^editor/(?P<fname>\w+)/$', views.editor, name='editor'),
    path('editor/<str:fname>/',views.editor, name='editor'),
    path('',views.index, name='index'),
]