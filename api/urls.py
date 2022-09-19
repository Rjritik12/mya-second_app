from django.contrib import admin
from django.urls import path
from restapi import views
from rest_framework.urlpatterns import format_suffix_patterns

  
# urlpatterns = [
#     path('transformers/', views.TransformerList.as_view()),
#     path('transformers/<int:pk>/', views.TransformerDetail.as_view()),
# ]
  
# urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('api/',views.ourdata.as_view()),
    path('api/<int:pk>/',views.ourdata.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
