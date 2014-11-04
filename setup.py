import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = ('Arche',
            )


setup(name='arche_video',
      version='0.1dev',
      description='Arche video',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Intended Audience :: Developers",
        ],
      author='Robin Harms Oredsson and contributors',
      author_email='robin@betahaus.net',
      url='',
      keywords='web pyramid pylons arche',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="arche_video",
      entry_points = """\
      [fanstatic.libraries]
      arche_video = arche_video.fanstatic_lib:library
      """,
      )
