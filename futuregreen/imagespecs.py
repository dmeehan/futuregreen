# futuregreen/imagespecs.py

from imagekit.specs import ImageSpec
from imagekit import processors

class ResizeAdminThumbnail(processors.Resize):
    width = 120
    height = 67
    crop = True

class ResizeProjectThumbnail(processors.Resize):
    width = 80
    height = 80
    crop = True

class ResizeProjectList(processors.Resize):
    width = 180
    height = 180
    crop = True

class ResizeProjectDetail(processors.Resize):
    width = 780
    height = 380
    crop = True

class ResizeProjectMax(processors.Resize):
    width = 1080

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

class ProjectThumbnail(ImageSpec):
    pre_cache = False
    processors = [ResizeProjectThumbnail, EnhanceSmall]

class ProjectList(ImageSpec):
    pre_cache = False
    processors = [ResizeProjectList]

class ProjectDetail(ImageSpec):
    pre_cache = False
    processors = [ResizeProjectDetail]