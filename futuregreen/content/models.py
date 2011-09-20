# content/models.py
from blocks.models import TextBlockBase
from images.models import ImageFieldAutoMixin

from futuregreen.portfolio import Project

class ContentBlock(ImageFieldAutoMixin, TextBlockBase):
    pass

