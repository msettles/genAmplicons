#!/usr/bin/env python


try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension


editdist = Extension('editdist', sources=['lib/editdist.c'])
trim = Extension('trim', sources=['lib/trim.c'])

config = \
    {
        'description': 'Processing of Illumina amplicon projects - generic version',
        'author': 'Matt Settles',
        'url': 'https://github.com/msettles/genAmplicons',
        'download_url': 'https://github.com/msettles/genAmplicons',
        'author_email': 'settles@ucdavis.edu',
        'version': 'v0.0.1-12132015',
        'install_requires': ['biom-format>=2.1.3', 'h5py'],
        'packages': ['genAmplicons'],
        'scripts': ['bin/genAmplicons'],
        'name': 'genAmplicons',
        "ext_package": 'genAmplicons',
        'ext_modules': [editdist, trim]
    }

setup(**config)
