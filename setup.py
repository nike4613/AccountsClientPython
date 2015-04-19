from setuptools import setup

import sys
if sys.version_info<(2,6,0):
  sys.stderr.write("You need python 2.6 or later to run this script\n")
  exit(1)

setup(
  name='AccountsClientPython',
  version='0.31',
  description="A python version of Mojang's AccountsClient repository with some extra features",
  install_requires=['requests'],
  author='DaNike4613',
  author_email='aaron.cirr.com@gmail.com',
  packages=['AccountsClientPython']
)
