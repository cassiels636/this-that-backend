from django.urls import path
from .views import ListThisNamesView, ListThatNamesView, RandomPairingView

urlpatterns = [
    path('thisnames/', ListThisNamesView.as_view(), name="this-all"),
    path('thatnames/', ListThatNamesView.as_view(), name="that-all"),
    path('randpairing/', RandomPairingView.as_view({'get': 'list'}), name="rand-pairing")
]
