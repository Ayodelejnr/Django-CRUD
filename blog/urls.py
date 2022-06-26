import django


from django.urls import path
from .views import blogAppCreateView, blogAppDetailView, blogAppListView, blogAppUpdateView




urlpatterns = [
    path(' ' ,blogAppCreateView.as_view(),
    name='home'),
    path('list/', blogAppListView.as_view()),
    path('detail/<pk>/', blogAppDetailView.as_view()),
    path('<pk>/update', blogAppUpdateView.as_view()),
    path('delete/<pk>/', blogAppDeleteView.as_views())
]