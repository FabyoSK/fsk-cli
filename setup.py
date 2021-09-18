from setuptools import setup

setup(
  name='fsk',
  version=1.0,
  packages=['fsk'],
  install_requires=[],
  entry_points={'console_scripts': ['fsk = fsk.cli.scripts.main:main']}
)