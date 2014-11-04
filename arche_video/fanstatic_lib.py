from fanstatic import Library
from fanstatic import Resource
from js.jquery import jquery


library = Library('arche_video', 'static')

mediaelement = Resource(library, 'mediaelement/mediaelement.js', depends = (jquery,))
mediaelement_and_player = Resource(library, 'mediaelement/mediaelement-and-player.js',
                                   minified = 'mediaelement/mediaelement-and-player.min.js', depends = (jquery,))
mediaelementplayer_css = Resource(library, 'mediaelement/mediaelementplayer.css',
                                  minified = 'mediaelement/mediaelementplayer.min.css')
mejs_skins = Resource(library, 'mediaelement/mejs-skins.css')
