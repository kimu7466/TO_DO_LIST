from django.db import models

# Create your models here.

class BaseClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Counter(BaseClass):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.count}"

class Tasks(BaseClass):
    title = models.CharField(max_length=100, blank=True)
    task = models.TextField(max_length=10000)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.title:
            counter = Counter.objects.get(id = 1)
            counter.count = counter.count + 1
            counter.save()
            self.title = f"TITLE : {counter.count}"

        super(Tasks, self).save(*args, **kwargs)