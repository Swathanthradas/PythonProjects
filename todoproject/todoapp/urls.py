from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvlist/',views.tasklistview.as_view(),name='cbvlist'),
    path('detailv/<int:pk>/',views.taskdetailview.as_view(),name='detailv'),
    path('cbvupdate/<int:pk>/',views.taskupdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.taskdeleteview.as_view(),name='cbvdelete')
]