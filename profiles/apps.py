from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
    
    def ready(self):
        import profiles.signals
        
        
# we need to add default_app_config = 'profiles.apps.ProfilesConfig' this to the __init__.py file
# if we have used any custom config in the apps.py file