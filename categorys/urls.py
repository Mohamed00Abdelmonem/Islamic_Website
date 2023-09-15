from django.urls import path
from .views import MainTopicList, TopicDetail


urlpatterns = [
    path('<int:pk>', MainTopicList.as_view()),
    path('topic/<int:pk>', TopicDetail.as_view()),

]