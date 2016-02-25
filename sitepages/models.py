from django.db import models
from django.db.models.signals import post_save
# Create your models here.


class TestModel(models.Model):
    name = models.CharField(max_length=255)


class TestModel2(models.Model):
    groupname = models.CharField(max_length=255)


def save_group(sender, instance, created, **kwargs):
    TestModel2.objects.create(groupname=instance.name)

post_save.connect(save_group, sender=TestModel)
