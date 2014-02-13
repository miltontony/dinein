from django.contrib.auth.models import User
from dinein.social.models import Person

User.profile = property(
    lambda u: Person.objects.get_or_create(username=u.username)[0]
)
