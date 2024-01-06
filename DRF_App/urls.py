from django import views
from django.urls import include, path
from .views import Books, Student
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     # path("", home.as_view(), name="home"),
#     path("books/", BookList.as_view(), name="book-list"),
#     path("books/<int:pk>/", BookDetail.as_view(), name="book-detail"),
# ]


route = DefaultRouter()
route.register(r'books', Books, basename='book'),
route.register(r'student', Student, basename='student')


urlpatterns = [
    path("api/", include(route.urls)),

]
