from django.db import models

# Create your models here.


class Do_list(models.Model):
    content = models.CharField(max_length=50)
    information = models.TextField()
    pub_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True)
    check = models.BooleanField(default=False)
    state = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}. {self.content}"
