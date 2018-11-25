#developer's defined URLs
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from  . import views

router=DefaultRouter()

#defining and register urls of viewset to default router
router.register('movie', views.MovieViewSet)
router.register('user', views.UserProfileViewSet)
router.register('login',views.LoginViewSet, base_name='login')

urlpatterns=[    
    #path('movies/',views.MoviesApiView),
    path('',include(router.urls)),
    
]