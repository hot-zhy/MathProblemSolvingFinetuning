from setuptools import setup, find_packages

setup(name='pal',
      version='0.1',
      description='PAL',
      packages=['pal', 'pal.core', 'pal.prompt'],
      install_requires=['openai', 'python-dateutil'],
)