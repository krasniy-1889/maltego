from django.core.management import BaseCommand

from apps.user.models import User


class Command(BaseCommand):
    help = "Create an admin user"

    def handle(self, *args, **options):
        # Your logic to create the admin user goes here
        username = "jake"
        password = "jewel"
        email = "jake@pandora.navi"
        User.objects.create_superuser(username, email, password)
        self.stdout.write(self.style.SUCCESS("Admin user created successfully!"))
