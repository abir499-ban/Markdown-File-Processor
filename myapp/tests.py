from django.test import TestCase
import os
from django.conf import settings
# Create your tests here.
directory = os.path.join(settings.BASE_DIR, 'uploads')
print(os.listdir(directory))
