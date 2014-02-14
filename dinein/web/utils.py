import re
from django.template.defaultfilters import slugify


RE_NUMERICAL_SUFFIX = re.compile(r'^[\w-]*-(\d+)+$')


def generate_slug(cls, obj, text, tail_number=0):
    """
    Returns a new unique slug. Object must provide a SlugField called slug.
    URL friendly slugs are generated using django.template.defaultfilters'
    slugify. Numbers are added to the end of slugs for uniqueness.
    """
    # use django slugify filter to slugify
    slug = slugify(text)

    # Empty slugs are ugly (eg. '-1' may be generated) so force non-empty
    if not slug:
        slug = 'no-title'

    values_list = cls.objects.filter(
        slug__startswith=slug
    ).values_list('id', 'slug')

    # Find highest suffix
    max = -1
    for tu in values_list:
        if tu[1] == slug:
            if tu[0] == obj.id:
                # If we encounter obj and the stored slug is the same as the
                # desired slug then return.
                return slug

            if max == -1:
                # Set max to indicate a collision
                max = 0

        # Update max if suffix is greater
        match = RE_NUMERICAL_SUFFIX.match(tu[1])
        if match is not None:

            # If the collision is on obj then use the existing slug
            if tu[0] == obj.id:
                return tu[1]

            i = int(match.group(1))
            if i > max:
                max = i

    if max >= 0:
        # There were collisions
        return "%s-%s" % (slug, max + 1)
    else:
        # No collisions
        return slug
