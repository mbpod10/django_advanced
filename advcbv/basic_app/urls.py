from django.urls import path, include
from basic_app import views

app_name = 'basic_app'  # <<<<<< HERE

# READ
# Go to 'basic_app_base.html' and see that url tag in the template and it says BASIC_APP:LIST
# the 'basic_app' refers to the app name from above and 'list' refers to the NAME of the
# path below
######

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),  # <<< HERE
    path('<int:pk>/', views.SchoolDetailView.as_view(), name="detail"),
    path('create/', views.SchoolCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name="delete"),
]
