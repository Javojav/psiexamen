from django.shortcuts import render

# ai k meter estas vainas
from django.views import generic
from .models import Canal, Usuario, Suscripcion

from rest_framework import viewsets, status
from rest_framework.response import Response

from . import serializers

class CanalDetailView(generic.DetailView):
    model = Canal
    template_name = 'canal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombreCanal'] = Canal.objects.get(id=self.kwargs['pk']).nombreCanal

        context['suscripciones'] = Suscripcion.objects.filter(canal=self.kwargs['pk'])

        return context

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

    ## kreo k es optional
    def retrieve(self, request, *args, **kwargs):
        data = {
            "id" : int (kwargs.get('pk'))
        }

        u = Usuario.objects.filter(id=data['id'])
        if u.exists():
            
            serializer = self.serializer_class(u.first())

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, *args, **kwargs):

        u = Usuario.objects.all()
        if u.exists():
            
            serializer = self.serializer_class(u, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class SuscripcionViewSet(viewsets.ModelViewSet):
    queryset = Suscripcion.objects.all()
    serializer_class = serializers.SuscripcionSerializer

    def retrieve(self, request, *args, **kwargs):
        data = {
            "id" : int (kwargs.get('pk'))
        }

        s = Suscripcion.objects.filter(id=data['id'])
        if s.exists():
            
            serializer = self.serializer_class(s.first())

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, *args, **kwargs):

        s = Suscripcion.objects.all()
        if s.exists():
            
            serializer = self.serializer_class(s, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class CanalViewSet(viewsets.ModelViewSet):
    queryset = Canal.objects.all()
    serializer_class = serializers.CanalSerializer

    def retrieve(self, request, *args, **kwargs):
        data = {
            "id" : int (kwargs.get('pk'))
        }

        c = Canal.objects.filter(id=data['id'])
        if c.exists():
            
            serializer = self.serializer_class(c.first())

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, *args, **kwargs):

        c = Canal.objects.all()
        if c.exists():
            
            serializer = self.serializer_class(c, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)