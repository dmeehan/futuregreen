# content/models.py
from futuregreen.blocks.models import TextBlockBase
from futuregreen.images.models import ImageFieldAutoMixin

class ContentBlock(ImageFieldAutoMixin, TextBlockBase):
    pass

