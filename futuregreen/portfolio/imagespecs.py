# futuregreen/portfolio/imagespecs.py

from imagekit.specs import ImageSpec
from imagekit import processors

class ResizeAdminThumbnail(processors.Resize):
    width = 120
    height = 67
    crop = True

class EnhanceSmall(processors.Adjustment):
    contrast = 1.2
    sharpness = 1.1

# Next we define our specifications or "specs". Image specs are where we define
# the individual "classes" of images we want to have access to. Like processors
# image specs are configured by subclasses the ImageSpec superclass.

class AdminThumbnail(ImageSpec):
    access_as = 'admin_thumbnail'
    pre_cache = False
    processors = [ResizeAdminThumbnail, EnhanceSmall]