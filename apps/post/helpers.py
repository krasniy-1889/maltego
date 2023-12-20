from ..user.models import User
from cuid import cuid


# * Model Helpers
def chapter_page_upload_to(instance, filename):
    post_id = instance.post.id
    chapter_id = instance.chapter.id
    return f"{post_id}/{chapter_id}/{cuid()}{filename}"


def get_default_user():
    return User.objects.filter(is_superuser=True).first()
