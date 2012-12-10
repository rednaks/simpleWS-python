# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name = "simpleWSpy",
      version = '0.0.1',
      description = "A Simple WebSocket library for Python",
      maintainer = "Alexandre BM",
      maintainer_email = "s@rednaks.tn",
      url = "https://github.com/rednaks/simpleWS-python",
      download_url = "https://github.com/rednaks/simpleWS-python",
      packages = ["simpleWSpy", "simpleWSpy.server"],
      platforms = ["any"],
      license = 'GPLV3',
      long_description = "A Simple WebSocket library for Python",
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GPL V3 License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Topic :: Communications',
          'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
          'Topic :: Software Development :: Libraries :: Python Modules'
          ],
     )
