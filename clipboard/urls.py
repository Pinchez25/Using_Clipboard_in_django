from django.urls import path
from .views import QuotesList

urlpatterns = [
    path('',QuotesList.as_view(),name="quotes")
]
