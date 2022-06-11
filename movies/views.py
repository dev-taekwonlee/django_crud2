# import re
# from django.shortcuts import render

# Create your views here.

import json

from django.http import JsonResponse
from django.views import View

from movies.models import Movie, Actor, ActorMovie


class ActorView(View):
  def get(self, request):
    actors = Actor.objects.all()
    results = []

    for actor in actors:
      name = actor.last_name + actor.first_name

      actor_information = (
        {
          'name': name,
          'movies': [movie.title for movie in actor.movie_set.all()]
        }
      )

      results.append(actor_information)
    return JsonResponse({'actor': results}, status=200)

class MovieView(View):
  def get(self, request):
    movies = Movie.objects.all()
    results = []

    for movie in movies:
      title = movie.title
      runtime = movie.runtime

      movie_information = (
        {
          'title': title,
          'runtime': runtime,
          'actors': [actor.last_name + actor.first_name for actor in movie.actors.all()]
        }
      )
      results.append(movie_information)
    return JsonResponse({'movie': results}, status=200)

## 아래는 강의 내용 - 구동 안됨
# class ActorView(View):
#   def get(self, request):
#     result = []
#     actors = Actor.objects.all()

#     for actor in actors:
#       movie_list = []
#       movies = actor.movie.all()

#       for movie in movies:
#         movie_list.append(movie.title)
#       movie_information = {
#         'first_name': actor.first_name,
#         'last_name' : actor.last_name,
#         'movies'    : movie_list
#       }
#       result.append(movie_information)
#     return JsonResponse({'result':result}, status=200)


# class MovieView(View):
#   def get(self, request):
#     result = []
#     movies = Movie.objects.all()

#     for movie in movies:
#       actor_list = []
#       actors = movie.actor_set.all()

#       for actor in actors:
#         actor_list.append(actor.last_name + actor.first_name)
#       movie_information = {
#         'title' : movie.title,
#         'runtime' : movie.runtime,
#         'actors' : actor_list
#       }
#       result.append(movie_information)
#     return JsonResponse({'result': result}, status=200)
