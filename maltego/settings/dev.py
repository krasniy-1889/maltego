import os

try:
    from .base import *
except ImportError as e:
    print(e)

DEBUG = True
ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = [
    "127.0.0.1",
]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "maltego",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# S3 Storage
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "eAQojoueAhfznuemBHJ0")
AWS_SECRET_ACCESS_KEY = os.environ.get(
    "AWS_SECRET_ACCESS_KEY", "kaXyI1esXlZc3GSeFCYFXHDkL9V5femMScrM6Xmm"
)
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "django")
if DEBUG:
    AWS_S3_ENDPOINT_URL = "http://localhost:9000"
