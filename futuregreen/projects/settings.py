# projects/settings.py

from django.conf import settings

DEFAULT_SETTINGS = {
    'PROJECT_MODEL': 'projects.default_models.Project',
    'PROJECT_MARKUP': '',
    'PROJECT_PAGINATE_BY': 10,
}

DEFAULT_SETTINGS.update(getattr(settings, 'PROJECTS_SETTINGS', {}))

# Add all the keys/values to the module's namespace
globals().update(DEFAULT_SETTINGS)