from arche.interfaces import IFile
from zope.interface import implementer

from arche_video.interfaces import INewVideo


@implementer(INewVideo)
class NewVideo(object):

    def __init__(self, video):
        assert IFile.providedBy(video), "Must be an object implementing IFile"
        self.video = video
