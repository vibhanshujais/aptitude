from django.db import models

class aptitude(models.Model):
    category = models.TextField()
    topic = models.TextField()
    question = models.TextField()
    option1 = models.TextField(null=True)
    option2 = models.TextField(null=True)
    option3 = models.TextField(null=True)
    option4 = models.TextField(null=True)
    option5 = models.TextField(null=True)
    answer = models.TextField()
    def __str__(self):
        return self.topic


class Category(models.Model):
    category = models.TextField()
    def __str__(self):
        return self.category
    
class algorithm(models.Model):
    category = models.TextField(null=True)
    name = models.TextField()
    def __str__(self):
        return self.name
    
class algo_category(models.Model):
    category = models.TextField()
    def __str__(self):
        return self.category
    

class vocabulary(models.Model):
    topic = models.TextField()
    category = models.TextField(null=True)
    question = models.TextField(null=True)
    answer = models.TextField(null=True)
    def __str__(self):
        return self.topic
    
class vocab_category(models.Model):
    category = models.TextField()
    def __str__(self):
        return self.category
    
