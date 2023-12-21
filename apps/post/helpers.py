from cuid import cuid
from django.contrib.auth import get_user_model


# * Model Helpers
def chapter_page_upload_to(instance, filename):
    post_id = instance.post.id
    chapter_id = instance.chapter.id
    return f"{post_id}/{chapter_id}/{cuid()}{filename}"


def get_default_user():
    return get_user_model().objects.filter(is_superuser=True).first()
