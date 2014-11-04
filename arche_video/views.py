from arche_video.fanstatic_lib import (mediaelementplayer_css,
                                       mediaelement_and_player,
                                       mejs_skins)
from arche.views.base import BaseView
from arche import security


class MediaPlayerView(BaseView):
    def __call__(self):
        mediaelementplayer_css.need()
        mediaelement_and_player.need()
        return {}


def includeme(config):
    config.add_view(MediaPlayerView,
                    name = '__media_player__',
                    context = 'arche.interfaces.IFile',
                    permission = security.PERM_VIEW,
                    renderer = 'arche_video:templates/video.pt')
    config.add_mimetype_view('video/*', '__media_player__')
