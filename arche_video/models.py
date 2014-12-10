from __future__ import unicode_literals

from arche.resources import Content
from arche.resources import DCMetadataMixin
from arche.interfaces import IBlobs

from arche_video import _


class VideoFolder(Content, DCMetadataMixin):
    type_name = "VideoFolder"
    type_title = _("Video folder")
    default_view = u"view"
    nav_visible = True
    listing_visible = True
    search_visible = True
    show_byline = True
    icon = "film"
    add_permission = "Add %s" % type_name

    @property
    def image_data(self):
        blobs = IBlobs(self, None)
        if blobs:
            return blobs.formdata_dict('image')
    @image_data.setter
    def image_data(self, value):
        IBlobs(self).create_from_formdata('image', value)


def includeme(config):
    config.add_content_factory(VideoFolder, addable_to = ('Document', 'Root', ), addable_in = ('File',))
