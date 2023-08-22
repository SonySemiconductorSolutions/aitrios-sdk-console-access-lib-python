# ------------------------------------------------------------------------
# Copyright 2022 Sony Semiconductor Solutions Corp. All rights reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------
"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject

Command to generate whl file <PACKAGE_NAME>-<PACKAGE_VERSION>-py2.py3-none-any.whl
python setup.py sdist bdist_wheel

"""
import logging
import sys
from pathlib import Path

from setuptools import find_packages, setup

try:
    # Check if file path is symbolic link
    symbolic_link = Path("README.md").is_symlink()
    if symbolic_link is True:
        sys.exit("The path to configuration file is a symbolic link")
    else:
        with open("README.md", "r", encoding="utf-8") as fh:
            long_description = fh.read()

except Exception as err:
    logging.error(str(err))
    logging.error("Configuration not loaded!!")
    raise err

SDK_SPECIFICATION_VERSION = "1.0.0"
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
        "requests>=2.31.0",
        "jsonschema>=4.6.2",
        "PyYAML>=6.0",
        "setuptools>=65.5.1",
        "wheel>=0.37.1",
        "PyJWT>=2.6.0",
        "nassl>=4.0",
        "cryptography>=36.0",
        "validators>=0.18",
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
