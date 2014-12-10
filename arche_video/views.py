from __future__ import unicode_literals

from arche import security
from arche.utils import generate_slug
from arche.views.base import BaseView
from arche.views.base import DefaultAddForm
from pyramid.httpexceptions import HTTPFound

from arche_video.fanstatic_lib import (mediaelementplayer_css,
                                       mediaelement_and_player,
                                       mejs_skins)


class MediaPlayerView(BaseView):
    def __call__(self):
        mediaelementplayer_css.need()
        mediaelement_and_player.need()
        return {}


class AddVideoFolderForm(DefaultAddForm):
    type_name = "VideoFolder"

    def save_success(self, appstruct):
        self.flash_messages.add(self.default_success, type="success")
        initial_video_data = appstruct.pop('initial_video_data')
        file_appstruct = {'file_data': initial_video_data}
        file_fact = self.get_content_factory('File')
        file_obj = file_fact(**file_appstruct)
        #Construct video folder
        factory = self.get_content_factory(self.type_name)
        obj = factory(**appstruct)
        name = generate_slug(self.context, obj.title)
        self.context[name] = obj
        #Add initial video file
        file_name = generate_slug(obj, file_obj.filename)
        obj[file_name] = file_obj
        return HTTPFound(location = self.request.resource_url(obj))


def includeme(config):
    config.add_view(MediaPlayerView,
                    name = '__media_player__',
                    context = 'arche.interfaces.IFile',
                    permission = security.PERM_VIEW,
                    renderer = 'arche_video:templates/video.pt')
    config.add_mimetype_view('video/*', '__media_player__')

def include_video_folder(config):
    config.add_view(AddVideoFolderForm,
                    context = 'arche.interfaces.IContent',
                    name = 'add',
                    request_param = "content_type=VideoFolder",
                    permission = security.NO_PERMISSION_REQUIRED, #perm check in add
                    renderer = 'arche:templates/form.pt')
    config.add_view(MediaPlayerView,
                    name = 'view',
                    context = 'arche_video.models.VideoFolder', #FIXME
                    permission = security.PERM_VIEW,
                    renderer = 'arche_video:templates/video_folder.pt')
