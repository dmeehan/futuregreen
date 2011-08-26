# blocks/models.py

from blocks.models import TextBlockBase
from images.models import ImageFieldAutoMixin

class ContentBlock(ImageFieldAutoMixin, TextBlockBase):
    pass

