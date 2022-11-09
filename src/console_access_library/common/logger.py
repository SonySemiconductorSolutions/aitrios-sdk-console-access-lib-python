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

# pylint:disable=wrong-import-position
# pylint:disable=duplicate-code
# pylint:disable=too-few-public-methods
# pylint:disable=missing-module-docstring
# pylint:disable=import-error
# pylint:disable=missing-function-docstring
# pylint:disable=missing-class-docstring

import contextlib
import logging
import pickle
import sys
import time
from datetime import datetime, timezone
from logging.handlers import TimedRotatingFileHandler

loggers = {}


class Logger:
    """
    Generic log class with custom log configuration. which abstracts \
    original logging for customization. it supports logs printed stdout and \
    to the log file.

        Example:
            .. code-block:: python

                from common.logger import Logger
                logger = Logger.set_logger
                class XYZ:
                    def XYZ():
                        logger.debug("")
                        logger.info("")
                        logger.error("")
    """

    CLIENT_NAME = "ConsoleAccessClient"
    FORMATTER = logging.Formatter(
        f"{datetime.now(timezone.utc).isoformat()} %(levelname)s {CLIENT_NAME}: %(message)s"
    )
    time_string = time.strftime("%Y%m%d-%H%M%S")
    LOG_FILE = f"console_access_library-{time_string}.log"
    DEBUG = logging.DEBUG
    WARNING = logging.WARNING
    INFO = logging.INFO
    ERROR = logging.ERROR
    OFF = 100
    LOGGER_NAME = __name__

    @staticmethod
    def get_console_handler():
        """Returns console handler function which sends logging output to sys.stdout

        Returns:
            console_handler: StreamHandler object
        """
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(Logger.FORMATTER)
        return console_handler

    @staticmethod
    def get_file_handler():
        """
        Returns file handler function which sends logging output to file

        Returns
            file_handler : TimedRotatingFileHandler object
        """
        file_handler = TimedRotatingFileHandler(Logger.LOG_FILE, when="midnight")
        file_handler.setFormatter(Logger.FORMATTER)
        return file_handler

    @staticmethod
    def set_logger():
        """
        Returns logger instance

        Args:
            level(str) : Log level INFO, ERROR, WARN, DEBUG, OFF
                Eg: set_logger(__name__)

        Returns:
            object : logger object created with console and file handler is returned
        """

        # pylint:disable=invalid-name
        # pylint:disable=global-variable-not-assigned
        # pylint:disable=no-else-return

        global loggers

        level = Logger.OFF
        try:
            with open("log_level.pickle", "rb") as handle:
                log_level_dict = pickle.load(handle)
                level = int(log_level_dict["CONSOLE_LOG_LEVEL"])
        except KeyError:
            pass
        except FileNotFoundError:
            pass

        logger_name = Logger.CLIENT_NAME
        if loggers.get(logger_name):
            return loggers.get(logger_name)
        else:
            logger = logging.getLogger(logger_name)
            logger.handlers.clear()
            logger.setLevel(level)
            if level != Logger.OFF:
                logger.addHandler(Logger.get_console_handler())
                logger.addHandler(Logger.get_file_handler())
            logger.propagate = False
            loggers[logger_name] = logger
            return logger

