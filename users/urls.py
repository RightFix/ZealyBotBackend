from django.urls import path
from .views import CreateUser

urlpatterns = [
    path('', CreateUser.as_view(), name='create_user'),
    path('get_user/<int:pk>/', CreateUser.as_view(), name="get_user")
    # path('community/', ),
    # path('tasks/', ),
]
