# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 19:31:23 2017

@author: Roland Proud
"""

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()
    
setup(name='pyechoraw',
      version='1.0.0.dev1',
      description='Reads raw echosounder data',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        #'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        #'Topic :: Text Processing :: Linguistic',
      ],
      keywords='echosounder marine acoustics mask',
      url='https://github.com/rolandproud/pyechoraw',
      author='Roland Proud',
      author_email='rp43@st-andrews.ac.uk',
      license='MIT',
      packages=['pyechoraw'],
            install_requires=[
          'numpy',
      ],
      python_requires='>=3',
      include_package_data=True,
      zip_safe=False)