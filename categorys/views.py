from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import MainTopic, Topics
# Create your views here.

class MainTopicList(DetailView):
    model = MainTopic
    template_name = 'categorys/maintopic_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topics"] = Topics.objects.filter(maintopic=self.get_object())
        return context
    

class TopicDetail(DetailView):
    model = Topics
    template_name = 'categorys/topic_detail.html'

