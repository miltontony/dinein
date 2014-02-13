from neo4django.db import models


class Person(models.NodeModel):
    username = models.StringProperty(indexed=True)
    follows = models.Relationship(
        'self',
        rel_type='follows',
        related_name='followed_by'
    )
