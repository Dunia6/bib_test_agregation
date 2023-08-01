from django.urls import path
from .views import BookViewSet, TopAuthorsViewByLikes, TopAuthorsViewByViews


urlpatterns = [
    path('', BookViewSet.as_view({'get': 'list'}), name='books'),
    path('top-authorsbylikes/', TopAuthorsViewByLikes.as_view(), name='top-authorsbylikes'),
    path('top-authorsbyviews/', TopAuthorsViewByViews.as_view(), name='top-authorsbyviews'),
]
