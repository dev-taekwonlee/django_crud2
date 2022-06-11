from django.urls import path
from movies.views import MovieView, ActorView

urlpatterns = [
  path('', MovieView.as_view()),
  path('/movies', MovieView.as_view()),
  path('/actors', ActorView.as_view())
]
