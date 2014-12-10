from pyramid.i18n import TranslationStringFactory


_ = TranslationStringFactory('arche_video')


def includeme(config):
    config.include('.views')

def video_folder(config):
    config.include('.views.include_video_folder')
    config.include('.models')
    config.include('.schemas')
