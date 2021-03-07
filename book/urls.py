from django.urls import path
from . import views 

app_name = 'book' 

urlpatterns = [
    path('list/', views.BookListView.as_view(), name='list'), 
    path('detail/<int:pk>/', views.BookDetailView.as_view(), name='detail'), 
    path('create/', views.BookCreateView.as_view(), name='create'), 
    path('update/<int:pk>/', views.BookUpdateView.as_view(), name='update'), 
    path('delete/<int:pk>/', views.BookDeleteView.as_view(), name='delete'),
    path('rlist/', views.ReferenceListView.as_view(), name='rlist'), 
    path('rdetail/<int:pk>/', views.ReferenceDetailView.as_view(), name='rdetail'), 
    path('rcreate/', views.ReferenceCreateView.as_view(), name='rcreate'), 
    path('rupdate/<int:pk>/', views.ReferenceUpdateView.as_view(), name='rupdate'), 
    path('rdelete/<int:pk>/', views.ReferenceDeleteView.as_view(), name='rdelete'),
]