from django.db import models
from django.contrib.auth.models import User 

status = [
  (1, 'BACKLOG'),
  (2, 'TO DO'),
  (3, 'DOING'),
  (4, 'TEST'),
  (5, 'DONE')
]

issue = [
  (1, 'HIGH'),
  (2, 'MEDIUM'),
  (3, 'LOW')
]


# Create your models here.
class Drf(models.Model):
  title = models.CharField(max_length=200) 
  description = models.TextField(blank=True)                       
  state = models.IntegerField(null=False, blank=False, choices=status)
  priority = models.IntegerField(null=False, blank=False, choices=issue)
  deliver_date = models.DateField(auto_now_add=False)
  comment = models.TextField(blank=True)
  # user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title  + ' by ' + self.user.username


