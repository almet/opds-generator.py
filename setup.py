import codecs
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    README = f.read()

REQUIREMENTS = [
    'yaml',
    'jinja2',
]

setup(name='opds-generator',
      version='0.0.1',
      description='OPDS Generator',
      long_description=README,
      license='Apache License (2.0)',
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: Implementation :: CPython",
          "Topic :: Internet :: WWW/HTTP",
          "License :: OSI Approved :: Apache Software License"
      ],
      keywords="OPDS generator",
      author='Alexis Metaireau',
      author_email='alexis@notmyidea.org',
      url='https://github.com/almet/opml-generator.py',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=REQUIREMENTS)
