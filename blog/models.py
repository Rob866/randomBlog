from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status="published")


class Post(models.Model):
    tags= TaggableManager()
    STATUS_CHOICES = (('draft','Borrador'),('published','Publicado'))
    title = models.CharField("titulo",max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author= models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body = models.TextField("contenido")
    publish = models.DateTimeField("publicado",default=timezone.now)
    created = models.DateTimeField("creado",auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 
    status= models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    imagen = models.ImageField(upload_to='post_image/%Y/%m/%d',blank=True)

    objects = models.Manager()
    published= PublishedManager() 
   
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.publish.year,self.publish.month,self.publish.day,
        self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    name = models.CharField("Nombre",max_length=50)
    email = models.EmailField()
    body  = models.TextField("Comentario")
    created =  models.DateTimeField("Creado",auto_now_add=True)
    updated =  models.DateTimeField("Actualizacion",auto_now=True)
    activate =  models.BooleanField("Activo",default=True)

    class Meta:
        ordering =("created",)

    def __str__(self):
        return f'Comentario de {self.name} en {self.post}'    

  

     




