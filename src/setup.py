"""
Copyright 2022 Sony Semiconductor Solutions Corp. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject

Command to generate whl file <PACKAGE_NAME>-<PACKAGE_VERSION>-py2.py3-none-any.whl
python setup.py sdist bdist_wheel

"""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

SDK_SPECIFICATION_VERSION = "0.1.0"
PACKAGE_VERSION = f"{SDK_SPECIFICATION_VERSION}"
PACKAGE_NAME = "console_access_library"
AUTHOR_NAME = "Sony Semiconductor Solutions Corp"
AUTHOR_EMAIL = "ashish.mahapatra@sony.com"

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Console Access Library",
    license="Apache License Version 2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "marshmallow>=3.17.0",
        "requests>=2.25.1",
        "jsonschema>=4.6.2",
        "PyYAML>=6.0",
        "setuptools>=63.1.0",
        "wheel>=0.37.1",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: Apache License Version 2.0",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(),
    python_requires=">=3.6, <4",
)
