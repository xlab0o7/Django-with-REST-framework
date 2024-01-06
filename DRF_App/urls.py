from django import views
from django.urls import include, path
from .views import Books
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     # path("", home.as_view(), name="home"),
#     path("books/", BookList.as_view(), name="book-list"),
#     path("books/<int:pk>/", BookDetail.as_view(), name="book-detail"),
#     path("testing/",
#          Books.as_view({'get': 'list', 'post': 'create'}), name="book"),
# ]


route = DefaultRouter()
route.register(r'books', Books, basename='book')

urlpatterns = [
    path("api/", include(route.urls)),

]
