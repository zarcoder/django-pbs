# Copyright 2008 VPAC
#
# This file is part of django-pbs.
#
# django-pbs is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# django-pbs is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with django-pbs  If not, see <http://www.gnu.org/licenses/>.

# Django settings for django_pbs project.
from os import path as os_path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Sam Morrison', 'sam@vpac.org'),
)

# A list of all PBS servers to list on the server list page
# also used when finding all jobs for a specific user.
LOCAL_PBS_SERVERS = ['brecca-m.vpac.org', 
                     'tango-m.vpac.org',
                     'edda-m.vpac.org',
                     'wexstan.vpac.org',
                     'wem-mgt.vpac.org',
                     'karros-m.vpac.org',]


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be avilable on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Australia/Melbourne'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-au'


MANAGERS = ADMINS

PROJECT_DIR = os_path.abspath(os_path.split(__file__)[0])
BASE_URL = ''



SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os_path.join(PROJECT_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/pbs_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '87zm7t34p6!^c--!3sii8j9u-@2_xd5q-bv-k0k@%pv6=82w9-'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    #'django.core.context_processors.debug',
    'django.core.context_processors.media',
)


ROOT_URLCONF = 'django_pbs.urls'

TEMPLATE_DIRS = (
    os_path.join(PROJECT_DIR, 'templates')
)


INSTALLED_APPS = (
    'django_common',
    'django_common.layout',
    'django_pbs.servers',
    'django_pbs.moab',
    'django_pbs',
)
