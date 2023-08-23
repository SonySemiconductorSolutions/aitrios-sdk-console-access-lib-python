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

# pylint:disable=missing-module-docstring
# pylint:disable=global-statement
# pylint:disable=global-variable-not-assigned
# pylint:disable=duplicate-code

import logging
from datetime import datetime

# the stream handler for console_access_library.
LOGGER_HANDLER = None
LIBRARY_NAME = "console_access_library"


def set_logger(level="DEBUG"):
    """
    Adds the specified level of stream handler to the logging module.
    Also, by specifying the ``OFF`` level, log output is disabled.
    Args:
        level (str): Logging level, e.g. ``DEBUG``
    """
    global LOGGER_HANDLER
    global LIBRARY_NAME

    if check_loglevel(level) is False:
        raise ValueError("Undefined log level")
    logger = logging.getLogger(LIBRARY_NAME)

    if LOGGER_HANDLER is None:
        LOGGER_HANDLER = logging.StreamHandler()
    else:
        logger.removeHandler(LOGGER_HANDLER)
        LOGGER_HANDLER = logging.StreamHandler()

    if level != "OFF":
        logger.setLevel(level)

        # Log format: 2022-06-21T11:31:42.612+0900 ERROR ConsoleAccessClient
        # Log format: 2022-11-03T20:46:41.961330 ERROR console_access_library get_devices
        log_format = f"{datetime.now().isoformat()} %(levelname)s ConsoleAccessClient %(message)s"
        date_format = "%Y-%m-%dT%H:%M:%S"
        LOGGER_HANDLER.setLevel(level)
        formatter = logging.Formatter(fmt=log_format, datefmt=date_format)
        LOGGER_HANDLER.setFormatter(formatter)
        logger.addHandler(LOGGER_HANDLER)


def check_loglevel(level):
    """check if log level is permitted"""
    permitted_log_lebel = [
        "DEBUG",
        logging.DEBUG,
        "INFO",
        logging.INFO,
        "WARNING",
        logging.WARNING,
        "ERROR",
        logging.ERROR,
        "OFF",
    ]
    return level in permitted_log_lebel


logging.getLogger(LIBRARY_NAME).addHandler(logging.NullHandler())
