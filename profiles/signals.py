from .models  import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save # this is a signal that gets fired after an object is saved
from django.dispatch import receiver # this is a decorator that gets the signal and performs some task

@receiver(post_save, sender=User) # this is a decorator that gets the signal and performs some task
def create_profile(sender, instance, created, **kwargs):
    print('created', created)
    print('instance', instance)
    print('sender', sender)
    if created:
        Profile.objects.create(user=instance)
        

# this is used to create a profile for each user that is created from the admin panel 

# and signals is basically a way to allow certain senders to notify a set of receivers that some action has taken place
# so based on that action we can dp some task

# and it will be having in case of creating a  user we will be having a presave and a postsave signal
# and in case of updating a user we will be having a preupdate and a postupdate signal
# presave is used to do some task before saving the user and postsave is used to do some task after saving the user
# so in our case we need to add the user to the profiles model after createing the user from the admin panel so we have used postsave signal

# and the receiver is a decorator that gets the signal and performs some task
# instance is the user that is created
# created is a boolean that is true if the user is created and false if the user is updated
# sender is the model that sends the signal
# kwargs is a dictionary of arguments ( keyword arguments - key value pairs)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# and after creating the signal we need to register the signal in the apps.py file
# by overwriting the ready method of the ProfilesConfig class in the apps.py file