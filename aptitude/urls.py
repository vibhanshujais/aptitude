"""
URL configuration for aptitude project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aptitude import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('quants',views.quants),
    path('reasoning',views.reasoning),
    path('english',views.english),
    path('quants/<str:topic_name>',views.questions,name='quants_questions'),
    path('english/<str:topic_name>',views.questions,name='english_questions'),
    path('reasoning/<str:topic_name>',views.questions,name='reasoning_questions'),
    path('blogs',views.blogs),
    path('algorithm',views.algo),
    path('algorithm/<str:algo_name>',views.algorithms,name='algorithm'),
    path('vocabulary',views.vocabs),
    path('vocabulary/<str:topic>',views.vocab,name='vocab'),
]
