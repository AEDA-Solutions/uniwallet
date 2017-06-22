#!/usr/bin/env python

from distutils.core import setup

setup(name='blockchain',
      version='1.4.0',
      description='Blockchain API library (v1)',
      author='Blockchain.info',
      author_email='support@blockchain.zendesk.com',
      url='https://github.com/blockchain/api-v1-client-python',
      license='MIT',
      packages=['blockchain', 'blockchain/v2'],
      keywords='blockchain.info api blockchain',
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Office/Business :: Financial",
        "License :: OSI Approved :: MIT License",
        ],
)
