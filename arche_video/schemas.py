import colander
import deform
from arche.schemas import BaseSchema
from arche.schemas import DCMetadataSchema
from arche.validators import supported_thumbnail_mimetype
from arche.widgets import FileAttachmentWidget

from arche_video import _


class EditVideoFolderSchema(BaseSchema, DCMetadataSchema):
    image_data = colander.SchemaNode(deform.FileData(),
                                         missing = None,
                                         title = _(u"Image"),
                                         blob_key = 'image',
                                         validator = supported_thumbnail_mimetype,
                                         widget = FileAttachmentWidget())


class AddVideoFolderSchema(EditVideoFolderSchema):
    initial_video_data = colander.SchemaNode(deform.FileData(),
                                     title = _(u"Initial video file"),
                                     widget = FileAttachmentWidget())


def includeme(config):
    config.add_content_schema('VideoFolder', AddVideoFolderSchema, 'add')
    config.add_content_schema('VideoFolder', EditVideoFolderSchema, 'edit')
