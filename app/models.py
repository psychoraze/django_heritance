from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    pic = models.ImageField(upload_to='pics', blank=True)
    story = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'

class Post(models.Model):
    user = models.CharField(max_length=10)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to = 'pics', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='Posts')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'