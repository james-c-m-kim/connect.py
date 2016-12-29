from setuptools import setup, find_packages
from connect import __version__ as version

with open('requirements.txt') as f:
    requirements = f.readlines()

with open('README.md') as f:
    readme = f.read()

setup(name='connect.py',
      author='GiovanniMCMXCIX',
      url='https://github.com/GiovanniMCMXCIX/connect.py',
      version=version,
      packages=find_packages(),
      license='MIT',
      description='An API wrapper for Monstercat Connect written in Python.',
      long_description=readme,
      include_package_data=True,
      install_requires=requirements,
      classifiers=[
          "Development Status :: 3 - Alpha",
          'License :: OSI Approved :: MIT License',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Internet',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',
      ]
      )