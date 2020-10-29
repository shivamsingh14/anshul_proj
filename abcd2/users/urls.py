from django.urls import include, path
from abcd2.users import views

urlpatterns = [
    path('', views.UserView.as_view())
]
