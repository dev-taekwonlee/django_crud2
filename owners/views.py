from django.shortcuts import render

# Create your views here.

import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnerView(View):
  def post(self, request):
    try:
      data = json.loads(request.body)

      owner_name = data['name']
      owner_email = data['email']
      owner_age = data['age']

      Owner.objects.create(
        name = owner_name,
        email = owner_email,
        age = owner_age
      )
    except KeyError:
      return JsonResponse({'Message':'Bad Request'}, status=400)
    return JsonResponse({'Message':'Created'}, status=201)

  def get(self, request):
      owners = Owner.objects.all()
      result = []

      for owner in owners:
          dogs = owner.dog_set.all()
          dog_list = []

          for dog in dogs:
              dogs = owner.dog_set.all()
              dog_info = (
                  {
                      'name': dog.name,
                      'age': dog.age
                  }
              )
              dog_list.append(dog_info)
          result.append(
              {
                  'name': owner.name,
                  'age': owner.age,
                  'email': owner.email,
                  'my_dog': dog_list
              }

          )

      return JsonResponse({'result': result}, status=200)

class DogView(View):
  def post(self, request):
    try:
      data = json.loads(request.body)

      dog_owner = Owner.objects.get(name=data['owner'])
      dog_name = data['name']
      dog_age = data['age']

      Dog.objects.create(
        owner = dog_owner,
        name = dog_name,
        age = dog_age
      )
    except KeyError:
      return JsonResponse({'Message':'Bad Request'}, status=400)
    return JsonResponse({'Message':'Created'}, status=201)

  def get(self, request):
      dogs = Dog.objects.all()

      result = []
      for dog in dogs:
          result.append(
          {
            'name': dog.name,
            'age': dog.age,
            'owner': dog.owner.name
          }
        )
      return JsonResponse({'MESSAGE': result}, status=200)