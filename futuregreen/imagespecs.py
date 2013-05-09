# futuregreen/imagespecs.py

from imagekit.specs import ImageSpec
from imagekit import processors

class ResizeAdminThumbnail(processors.Resize):
    width = 120
    height = 67
    crop = True

class ResizeThumbnail(processors.Resize):
    width = 120
    height = 120
    crop = True

class ResizeList(processors.Resize):
    width = 360
    height = 360
    crop = True

class ResizeDetail(processors.Resize):
    width = 1600
    height = 1067
    crop = True

class ResizeFeatured(processors.Resize):
    width = 760
    height = 760
    crop = True

class ResizeTwoThirds(processors.Resize):
    width = 1200
    height = 277
    crop = True

class ResizeThird(processors.Resize):
    width = 720
    height = 341
    crop = True

class ResizeLetterbox(processors.Resize):
    width = 1600
    height = 904
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

class Thumbnail(ImageSpec):
    pre_cache = False
    processors = [ResizeThumbnail]

class List(ImageSpec):
    pre_cache = False
    processors = [ResizeList]

class Detail(ImageSpec):
    pre_cache = False
    processors = [ResizeDetail]

class Featured(ImageSpec):
    pre_cache = False
    processors = [ResizeFeatured]

class Main(ImageSpec):
    pre_cache = False
    processors = [ResizeTwoThirds]

class Aside(ImageSpec):
    pre_cache = False
    processors = [ResizeThird]

class Letterbox(ImageSpec):
    pre_cache = False
    processors = [ResizeLetterbox]
