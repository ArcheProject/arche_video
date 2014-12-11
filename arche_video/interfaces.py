from zope.interface import Attribute
from zope.interface import Interface


class INewVideo(Interface):
    video = Attribute("Video file")
