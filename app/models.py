from django.db import models

# Create your models here.


class Animal(models.Model):
    # fields of the model 
    nome = models.CharField(max_length = 200)
    peso = models.TextField()
    altura = models.CharField(max_length = 200)
    descricao = models.CharField(max_length = 200)
    imagem = models.ImageField(upload_to = 'img', blank = True, null = True)
    
    
    # with their title name
    def __str__(self):
        return self.nome
    
class Categoria(models.Model):
        
        # fields of the model
        nome = models.CharField(max_length = 200)
        def __str__(self):
            return self.nome