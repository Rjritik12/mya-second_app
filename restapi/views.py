from django.shortcuts import render,HttpResponse
from .models import *
from django.http import Http404
  
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import StudenSerializer
import requests
def home(request):
    res=requests.get('http://127.0.0.1:8000/api/1/')
    return HttpResponse(res)


class ourdata(APIView):
    def get_object(self, pk):
        try:
            return Emp.objects.get(id=pk)
        except Emp.DoesNotExist:
            raise Http404
    def get(self,request,pk,format=None):
        data_value = self.get_object(pk)
        serializer_data = StudenSerializer(data_value)
        return Response(serializer_data.data)

# class TransformerDetail(APIView):
#     """
#     Retrieve, update or delete a transformer instance
#     """
#     def get_object(self, pk):
#         # Returns an object instance that should 
#         # be used for detail views.
#         try:
#             return Transformer.objects.get(pk=pk)
#         except Transformer.DoesNotExist:
#             raise Http404
  
#     def get(self, request, pk, format=None):
#         transformer = self.get_object(pk)
#         serializer = TransformerSerializer(transformer)
#         return Response(serializer.data)
  
#     def put(self, request, pk, format=None):
#         transformer = self.get_object(pk)
#         serializer = TransformerSerializer(transformer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
#     def patch(self, request, pk, format=None):
#         transformer = self.get_object(pk)
#         serializer = TransformerSerializer(transformer,
#                                            data=request.data,
#                                            partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
  
#     def delete(self, request, pk, format=None):
#         transformer = self.get_object(pk)
#         transformer.delete()
#         return Response(status=status.HTTP_204_N