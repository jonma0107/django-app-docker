import json
from .models import Drf
from django.test import TestCase
from rest_framework import status

from rest_framework.test import APIClient # Esta libreria va a actuar como si fuera el FrontEnd

# from django.test.client import encode_multipart
from rest_framework.test import APIRequestFactory

from django.test.client import encode_multipart, RequestFactory


# Create your tests here.

class TestApi(TestCase):
    
    def test_1_post(self):
      client = APIClient()
      response = client.post(
        'https://web-service-tasks.onrender.com/api/list/',
        {        
          "title": "tarea test",
          "description": "descripcion test",
          "state": "TO DO",
          "priority": "HIGH",
          "deliver_date": "2023-02-21",
          "comment": "comentario test"
        },
        format='json')
      print(status.HTTP_201_CREATED, 'Task Created')
      # print(status)
      # print(response.status_code)
      # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      # self.assertEqual('refresh' in response.data.keys(), True)  
      # self.assertEqual('access' in response.data.keys(), True)  

    def test_2_tasks_list(self):
      client = APIClient()
      response = client.get(
        'https://web-service-tasks.onrender.com/api/list/'
        )
      print(status.HTTP_200_OK, 'Task List')
      # print(status) 

    def test_3_get_some_task(self):
      client = APIClient()
      response = client.get(
        'https://web-service-tasks.onrender.com/api/list/?key=value'
        )
      print(status.HTTP_200_OK, 'Some Task')
      # print(status)  
    
    def test_4_task_put(self):  
      factory = APIRequestFactory()
      request = factory.put('https://web-service-tasks.onrender.com/api/list/?key=value', {'title': 'remember to email dave'}, content_type='application/json') 
      print(status.HTTP_200_OK, 'Task Updated')

    def test_5_task_delete(self):  
      factory = APIRequestFactory()
      request = factory.delete(f'https://web-service-tasks.onrender.com/api/list/{self.id}', content_type='application/json') 
      print(status.HTTP_204_NO_CONTENT, 'Task Deleted') 
      # print(status) 

    def test_6_task_filter(self):
      client = APIClient()
      response = client.get(
        'https://web-service-tasks.onrender.com/api/list/?search=HIGH'
        )
      print(status.HTTP_200_OK, 'Task Filtered')  
      
    # def test_task_put(self): 
    #   factory = RequestFactory()
    #   data = {'title': 'remember to email dave'}
    #   content = encode_multipart('BoUnDaRyStRiNg', data)
    #   content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'
    #   request = factory.put(f'http://127.0.0.1:8000/api/list/{self.id}', content, content_type=content_type) 
    #   print(status.HTTP_200_OK, 'Task Updated')
      # print(status) 
