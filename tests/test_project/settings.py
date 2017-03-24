SECRET_KEY = 'notsecret'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'menus',
    'djangocms_text_ckeditor',
    'treebeard',
    'cms',
    'filer',
    'easy_thumbnails',
    'shop',
    'post_office',
    'cmsplugin_cascade',
    'rest_checkout',
    'test_project',
]

SITE_ID = 1
SHOP_APP_LABEL = 'test_project'
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', "English"),
    ('de', "German"),
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]
