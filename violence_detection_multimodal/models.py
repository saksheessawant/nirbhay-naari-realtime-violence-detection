from django.db import models

from django.db import models
from django.utils import timezone


class Video(models.Model):
    
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return ": " + str(self.videofile)
class Audio(models.Model):
    text= models.CharField(help_text="You may type your story here",max_length=10000,blank=True, default="")
    audiofile= models.FileField(upload_to='audios/', null=True, verbose_name="",blank=True)

    def __str__(self):
        return self.text + ": " + str(self.audiofile)

def user_directory_path(instance, filename):
    return 'posts/{0}/{1}'.format(instance.id, filename)




class Score(models.Model):
    result = models.PositiveBigIntegerField()
    def __str__(self):
        return str(self.result)