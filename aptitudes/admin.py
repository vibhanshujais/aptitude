from django.contrib import admin
from aptitudes.models import aptitude
from aptitudes.models import algorithm

class aptitudes(admin.ModelAdmin):
    data = ('category', 'topic', 'question', 'option1', 'option2', 'option3', 'option4', 'option5','answer')

admin.site.register(aptitude,aptitudes)

class algorithms(admin.ModelAdmin):
    data = ('name','category')
admin.site.register(algorithm,algorithms)