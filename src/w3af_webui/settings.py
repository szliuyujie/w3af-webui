#-*- coding: utf-8 -*-
import os.path
from datetime import timedelta
from django.utils.translation import ugettext_lazy as _

# ---------- Personal settings -----------------
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

#CREATE USER w3af_webui@localhost IDENTIFIED BY "w3af_webui";
#CREATE DATABASE w3af_webui CHARACTER SET utf8;
#GRANT ALL ON w3af_webui.* TO w3af_webui@localhost;
DATABASES = {
    'default': {
        'ENGINE'   : 'django.db.backends.mysql',
        'NAME'     : 'w3af_webui',
        'USER'     : 'w3af_webui',
        'PASSWORD' : 'w3af_webui',
        'HOST'     : '',
        'PORT'     : '3306',
        'OPTIONS'  : { 'init_command': 'SET storage_engine=INNODB; '
                                       'SET names utf8;' },
    }
}

# Full url, just for link in notification email
APP_URL = 'http://your_domain.net'

# Path for w3af reports and profiles in your system
HTML_REPORT_UPLOAD = '/var/local/w3af-webui'

# ----------- Advanced settings--------------
MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'

LANGUAGES = (
    ('ru', _('Russian')),
    ('en', _('English')),
)

# Path for localisation 
_PATH = os.path.abspath(os.path.dirname(__file__))
LOCALE_PATHS = (os.path.join(_PATH, 'locale'),)

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'
LANGUAGE_CODE = 'en-EN'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Default charset to use for all HttpResponse objects
DEFAULT_CHARSET = 'utf-8'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'
MEDIA_ROOT = (os.path.join(_PATH, 'media'),)

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"

STATIC_ROOT = os.path.join(_PATH, 'static')
# List of finder classes that know how to find static files in
# various locations.
#STATICFILES_FINDERS = (
#    'django.contrib.staticfiles.finders.FileSystemFinder',
#    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
#)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'yourw3afpasswordphrase'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

ROOT_URLCONF = 'w3af_webui.urls'

CARROT_BACKEND = "django"

# Path for test_coverage reports
COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(_PATH, 'cover')

# jcelery
BROKER_HOST = "localhost"
BROKER_PORT = 3306
BROKER_VHOST = "/"
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"
CELERYD_CONCURRENCY = 10
CELERYD_LOG_LEVEL = "INFO"
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"

# Table name for user profile
AUTH_PROFILE_MODULE = 'w3af_webui.Profile'

# Settings for email notification
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 25 # port for SMTP
#EMAIL_HOST = 'your-relay.domain.net' # SMTP relay for e-mail notification

# ----------W3af_webui particular settings--------------
# Login for first user. It will create after migrate command
# This user have all permission. Password will be the same as username, don't
# forget to change it
SUPERUSER_NAME = 'w3af_admin'

# Interface language selection
LANGUAGES = (
    ('ru', _('Russian')),
    ('en', _('English')),
)

SEVERITY_FILTER = (
            ('all', _('All'), ('Low', 'Medium', 'High', 'Information')),
            ('high', _('Hight'), ('High',)),
            ('medium_and_more', _('Medium and higher'), ('High', 'Medium',)),
            ('medium', _('Medium'), ('Medium',)),
            ('low', _('Low'), ('Low',)),
            ('information', _('Information'), ('Information',)),
            )

SEVERITY_DICT = dict([ (x[0], x[2]) for x in SEVERITY_FILTER])

# Set default language for interfase. This value must be in LANGUAGES tuple
DEFAULT_LANGUAGE = 'en'

# Default content of scan profile
SCAN_DEFAULT_PROFILE = "\n"

# This output plugin will be added automaticaly for all scans
W3AF_OUTPUT_PLUGIN = 'output.htmlFile' # default output plugin for all scans
W3AF_LOG_PLUGIN = 'output.textFile' # default log plugin for all scans

# Shell command for w3af scaner
W3AF_RUN = 'w3af_console'

# Notification about scan finish. You can write your own notification module and 
# link up it here. Data format: 
# {'label': 'notification name', 
#  'id': 'notification_string_id', 
#  'module': 'python module witch send notification'},
# The first value set as default
NOTIFY_MODULES = (
    {'label': _('None'), 'id': 'None', 'module': ''}, # status number 1 set as default
    {'label': _('e-mail'), 'id': 'Mail', 'module': 'w3af_webui.notification.send_mail'},
    {
        'label': _('e-mail, about vulnerabilities only'),
        'id': 'MailOnlyBad',
        'module': 'w3af_webui.notification.send_mail_only_bad',
    },
)

VULN_POST_MODULE = ''

# Week day name
WEEK_DAY_NAME = (_('Monday'), _('Tuesday'), _('Wednesday'), _('Thursday'),
                 _('Friday'), _('Saturday'), _('Sunday'))
# Scan statuses
TASK_STATUS_KEYS = ('free', 'lock',)
TASK_STATUS = dict(zip(TASK_STATUS_KEYS, range(1, len(TASK_STATUS_KEYS) + 1)))

#Report statuses
SCAN_STATUS_KEYS = ('in_process', 'done', 'fail')
SCAN_STATUS = dict(zip(SCAN_STATUS_KEYS, range(1, len(SCAN_STATUS_KEYS) + 1)))

# Scan repet types
SCAN_REPEAT_KEYS = (_('never'), _('daily'), _('weekly'), _('monthly'),)
SCAN_REPEAT = dict(zip(SCAN_REPEAT_KEYS, range(1, len(SCAN_REPEAT_KEYS) + 1)))

# Time delta for find scan
FSCAN_TDELTA = {
    'max': timedelta(seconds=62),
    'min': timedelta(seconds=1),
}
 # list of permission's codenames for group User 
user_permission_list = [
            # about scantask model
            'add_scantask',
            'change_scantask',
            'delete_scantask',
            # about scan model
            'add_scan',
            'change_scan',
            'delete_scan',
            # about vulnerabilitytype model
            'add_vulnerabilitytype',
            'change_vulnerabilitytype',
            'delete_vulnerabilitytype',
            # about vulnerability model
            'add_vulnerability',
            'change_vulnerability',
            'delete_vulnerability',
            # about profilestasks model
            #'add_profilestasks',
            #'change_profilestasks',
            #'delete_profilestasks',
        ]

 # list of permission's codenames for group Advanced User 
advanced_user_permission_list = user_permission_list + [
            # about profilestargets model
            'add_profilestargets',
            'change_profilestargets',
            'delete_profilestargets',
            # about target model
            'add_target',
            'change_target',
            'delete_target',
            # about scanprofile model
            'add_scanprofile',
            'change_scanprofile',
            'delete_scanprofile',
            # about profilestasks model
            'add_profilestasks',
            'change_profilestasks',
            'delete_profilestasks',
            # permition view statistic
            'view_stats',
        ]

# User permissions configuration
USER_GROUPS = ({
        'name': 'User',
        'permissions': user_permission_list,
    },
    {
        'name': 'Advanced user',
        'permissions': advanced_user_permission_list,
    },
)

# Name of one of the field for target page
TARGET_COMMENT_LABEL = _('Comment')

TEST_DISCOVERY_ROOT = os.path.join(_PATH, 'tests')
TEST_RUNNER = 'tests.runner.DiscoveryRunner'

# ----------End W3af_webui particular settings--------------
# ------import local settings-------------------------------
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(_PATH, 'templates'),
    HTML_REPORT_UPLOAD,
    '/usr/share/pyshared/django/contrib/admin/static/admin',
)

AUTH_MIDDLEWARE = ()
TEMPLATE_CONTEXT_PROCESSORS = ()
INSTALLED_APPS = ()
try:
     from local_settings import *
except Exception, e:
    print 'Can not find local settings: %s' % e

try:
     from extra_settings import * # optional settings with your own auth
except Exception, e:
    print 'Can not find extra settings: %s' % e
    AUTH_MIDDLEWARE = (
        'django.contrib.auth.middleware.AuthenticationMiddleware',
    )

MIDDLEWARE_CLASSES = ((
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',) +
    AUTH_MIDDLEWARE +
    ('django.middleware.doc.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'w3af_webui.middleware.I18NMiddleware',
    ))

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

INSTALLED_APPS += (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    #'django_any',

    'djcelery',
    #'ghettoq',
    'djkombu',

    'w3af_webui',
    'south',
    'django_extensions',
    #'django_coverage',
)

#import djcelery
#djcelery.setup_loader()
