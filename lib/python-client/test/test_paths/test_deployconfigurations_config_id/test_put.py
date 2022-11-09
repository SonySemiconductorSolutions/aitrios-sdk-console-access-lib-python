# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.paths.deployconfigurations_config_id import put  # noqa: E501
from aitrios_console_rest_client_sdk_primitive import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDeployconfigurationsConfigId(ApiTestMixin, unittest.TestCase):
    """
    DeployconfigurationsConfigId unit test stubs
        DeployByConfiguration  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = put.ApiForput(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
