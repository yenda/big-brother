import os

#
# Any machine specific settings when using development settings.
#

# Automatically figure out the ROOT_DIR and PROJECT_DIR.
DJANGO_PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
ROOT_DIR = os.path.abspath(os.path.join(DJANGO_PROJECT_DIR, os.path.pardir, os.path.pardir))
