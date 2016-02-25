# Example of Django Model post_save() signal

The Files to check out are:
* .sitepages/admin.py
* sitepages/models.py

Django models send out a signal automaticly. We catch that signal with our post_save.connect().
```python
post_save.connect(save_group, sender=TestModel)
```
In post_save our first argument is the name of the function we wish to call. I called this one save_group()
```python
def save_group(sender, instance, created, **kwargs):
    TestModel2.objects.create(groupname=instance.name)
```
Our sender argument is the name of the model of the signal we are listening for.

In save_group we have the arguments sender, instance, created, **kwargs.

From the save_group function we create a new object from the other model we want to build.

If there are fields that you wish to populate with information from the first model called, you can assign them in the arguments of .create from the instance argument. A simple example of this is filling the groupname field in the second model with the name field in the first model groupname=instance.name.
```python
TestModel2.objects.create(groupname=instance.name)
```

Here is the full relevant code:

```python
from django.db import models
from django.db.models.signals import post_save


class TestModel(models.Model):
    name = models.CharField(max_length=255)


class TestModel2(models.Model):
    groupname = models.CharField(max_length=255)


def save_group(sender, instance, created, **kwargs):
    TestModel2.objects.create(groupname=instance.name)

post_save.connect(save_group, sender=TestModel)
