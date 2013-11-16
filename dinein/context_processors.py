from django.conf import settings

def ga_profile_id(request):
    return {'GA_PROFILE_ID': settings.GA_PROFILE_ID}
