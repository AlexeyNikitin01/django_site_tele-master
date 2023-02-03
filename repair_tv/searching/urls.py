from django.urls import path

from .views import SearchResultsView

app_name = 'searching'
urlpatterns = [
    path('', SearchResultsView.as_view(), name='search_result'),
]
