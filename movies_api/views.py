from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from rest_framework import filters

from . import serializers
from . import models
from . import permissions

# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    
    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.MovieSerializer
    queryset = models.Movie.objects.all()
    #only the post owner can update the movie's info and only user can make a post
    permission_classes=(permissions.UpdateMovieInfo, IsAuthenticatedOrReadOnly)
    
    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
    
    filter_backends=(filters.SearchFilter,)
    search_fields=('title','director',)    

    #permission_classes=(permissions.UpdateMovie,)	
    #filter_backend=(filters.DjangoFilterBackend,)
    #filterset_class=MovieFilter        

    # def list(self,request):
    #     a_viewset=[
    #         'Uses actions (list, create, retrieve, update, partial update) ',
    #         'Automatically maps URLs using routers',
    #         'more functionality with less code'
    #     ]
    #     return Response({'message':'Movies', 'a_viewset':a_viewset})
    
    # def create(self,request):
    #     serializer = serializers.MovieSerializer(data=request.data)
    #     if serializer.is_valid():
    #         title=serializer.data.get('title')
    #         year=serializer.data.get('year')
    #         return Response({'message':f'Information about {title}({year}) is succesfully added to the database'})
    #     else:
    #         return Response(
    #             serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    # def retrieve(self,request,pk=None):
    #     return Response({'http_method:''GET'})
        
    # def update(self,request,pk=None):
    #     return Response({'http_method:''PUT'})
        
    # def partial_update(self,request,pk=None):
    #     return Response({'http_method:''PATCH'})
        
    # def destroy(self,request,pk=None):
    #     return Response({'http_method:''DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    
    serializer_class=serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    
    filter_backend=(filters.SearchFilter,)
    search_fields=('name','email',)

    # def list(self,request):
    #     a_viewset=[
    #         'Uses actions (list, create, retrieve, update, partial update) ',
    #         'Automatically maps URLs using routers',
    #         'more functionality with less code'
    #     ]
    #     return Response({'message':'Users', 'a_viewset':a_viewset})
    # def create(self,request):
    #     serializer = serializers.UserProfileSerializer(data=request.data)
    #     if serializer.is_valid():
    #         name=serializer.data.get('name')            
    #         return Response({'message':f'Information about user {name} is succesfully added to the database'})
    #     else:
    #         return Response(
    #             serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    # def retrieve(self,request,pk=None):
    #     return Response({'http_method:''GET'})
        
    # def update(self,request,pk=None):
    #     return Response({'http_method:''PUT'})
        
    # def partial_update(self,request,pk=None):
    #     return Response({'http_method:''PATCH'})
        
    # def destroy(self,request,pk=None):
    #     return Response({'http_method:''DELETE'})


class LoginViewSet(viewsets.ViewSet):
    serializer_class=AuthTokenSerializer

    def create(self,request):
        return ObtainAuthToken().post(request) #calling through viewset
    
# class MoviesApiView(APIView):
#     # API View is good for developer's-defined logic for the api    
#     serializer_class=serializers.MovieSerializer

#     def get(self, request, format=None):

#         an_apiview=[
#             'Uses HTTP methods as function(get,post,patch,put,delete)',
#             'Similar to Django pre-defined view',
#             'Gives control over your logic',
#             'Is mapped manually to URLs'
#         ]

#         return Response({'message': 'Movies!', 'an_apiview':an_apiview})

#     def post(self,request):
#         """add a movie's info to database"""

#         serializer = serializers.MovieSerializer(data=request.data)

#         if serializer.is_valid():
#             title=serializer.data.get('title')
#             year=serializer.data.get('year')            
#             duration=int(serializer.data.get('duration_minute'))
#             message=f'Information about {title}({year}) movie is successfully added to the database'
            
#             return Response({'message':message})        
#         else:
#             return Response(
#                 serializer.errors,status=status.HTTP_400_BAD_REQUEST
#             )
#     def put(self,request,pK=None):
        
#         serializer = serializers.MoviesSerializer(data=request.data)
#         if serializer.is_valid():
#             title=serializer.data.get('title')
#             year=serializer.data.get('year')
        
#             return Response({'message':f'Information about {title}({year}) is succesfully updated(put)'})
#         else:
#                 return Response(
#                 serializer.errors,status=status.HTTP_400_BAD_REQUEST
#             )
    
#     def patch(self,request,pK=None):
        
#         serializer = serializers.MoviesSerializer(data=request.data)
#         if serializer.is_valid():
#             title=serializer.data.get('title')
#             year=serializer.data.get('year')
#             return Response({'message':f'Information about {title}({year}) is succesfully updated(patch)'})
    
#     def delete(self,request,pK=None):
#         serializer = serializers.MoviesSerializer(data=request.data)
#         if serializer.is_valid():
#             title=serializer.data.get('title')
#             year=serializer.data.get('year')
#             return Response({'message':f'Information about {title}({year}) is succesfully deleted'})

# class UserProfilesApiView(APIView):
    #use APIView when you want to have full control of the logic

    
#     serializer_class=serializers.UserProfileSerializer

#     def get(self, request, format=None):

#         an_apiview=[
#             'Uses HTTP methods as function(get,post,patch,put,delete)',
#             'Similar to Django pre-defined view',
#             'Gives control over your logic',
#             'Is mapped manually to URLs'
#         ]
#         return Response({'message': 'User Profiles!', 'an_apiview':an_apiview})
    
#     def post(self,request):
#         """Say hello to the user"""

#         serializer = serializers.UserProfileSerializer(data=request.data)

#         if serializer.is_valid():
#             name=serializer.data.get('name')
#             email=serializer.data.get('email')
#             password=serializer.data.get('password')
#             password_confirmation=serializer.data.get('password_confirmation')
#             if password==password_confirmation:
#                 message=f'The user {name} is successfully added to the database'                
#             else:
#                 #message=f'Your password confirmation is different from your password'                
#                 raise ValueError('Your password confirmation is different from your password')        
#             return Response({'message':message})        
#         else:
#             return Response(
#                 serializer.errors,status=status.HTTP_400_BAD_REQUEST
#             )
#     def put(self,request,pK=None):
        
#         # serializer = serializers.UserProfilesSerializer(data=request.data)
#         # if serializer.is_valid():
#         #     name=serializer.data.get('name')                    
#         #     return Response({'message':f'Information about the user {name} is succesfully updated(put)'})
#         return Response({'message':f'Information about the user {name} is succesfully updated(put)'})
#     def patch(self,request,pK=None):
        
#         # serializer = serializers.UserProfilesSerializer(data=request.data)
#         # if serializer.is_valid():
#         #     name=serializer.data.get('name')            
#         #     return Response({'message':f'Information about the user {name} is succesfully updated(patch)'})
#         return Response({'message':f'Information about the user {name} is succesfully updated(patch)'})
    
#     def delete(self,request,pK=None):
#         # serializer = serializers.UserProfilesSerializer(data=request.data)
#         # if serializer.is_valid():
#         #     name=serializer.data.get('name')            
#         #     return Response({'message':f'Information about the user {name} is succesfully deleted'})
#         return Response({'message':f'Information about the user {name} is succesfully deleted'})

