try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'logfind',
    'author': 'Kevin Kalinowski',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'kalinowk@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['logfind'],
    'scripts': [],
    'name': 'logfind'
}

setup(**config)