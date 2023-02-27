from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Student
from django.contrib.auth.models import Group

@receiver(post_save, sender=User)
def student_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='student')
        instance.groups.add(group)

        Student.objects.create(
            user=instance,
            # firstname=instance.username
        )
        print('Profile created')

