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

# pylint:disable=missing-module-docstring
# pylint:disable=import-error
# pylint:disable=too-many-instance-attributes
# pylint:disable=too-many-public-methods
# pylint:disable=duplicate-code
# pylint:disable=redefined-builtin
# pylint:disable=too-many-arguments
# pylint:disable=too-many-locals
# pylint:disable=too-many-return-statements

from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass
from console_access_library.insight.get_image_directories import GetImageDirectories
from console_access_library.insight.get_images import GetImages
from console_access_library.insight.get_inference_results import GetInferenceresults


class Insight(ConsoleAccessBaseClass):
    """Abstract class to access Console Access Library Insight component APIs from Insight component

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for Insight Abstract class

        Args:
            config(object): Object of Configuration Class
        """
        super().__init__()
        self._get_image_directories_obj = GetImageDirectories(config)
        self._get_images_obj = GetImages(config)
        self._get_inference_results_obj = GetInferenceresults(config)

    def get_image_directories(self, device_id: str):
        """Abstract function call to ``get_image_directories`` API

        Args:
            device_id (str, required): Device ID. If specified, returns a list of image
                directories linked to the specified device ID.

        Returns:
            dict: Dictionary object returned by ``get_image_directories`` API
        """
        return self._get_image_directories_obj.get_image_directories(device_id)

    def get_images(
        self,
        device_id: str,
        sub_directory_name: str,
        number_of_images: int = None,
        skip: int = None,
        order_by: str = None,
    ):
        """Abstract function call to ``get_images`` API

        Args:
            device_id (str, required) : The Device ID.
            sub_directory_name (str, required) : The Sub Directory Name.
                The subdirectory will be the directory notified in the response
                of start_upload_inference_result.

            number_of_images (int, optional) : The Number Of Images. 0-256. If not specified: 50
            skip (int, optional) : The Skip. If not specified: 0
            order_by (str, optional) : The Order By. DESC, ASC, desc, asc. If not specified:ASC

        Returns:
            dict: Dictionary object returned by ``get_images`` API
        """
        return self._get_images_obj.get_images(
            device_id, sub_directory_name, number_of_images, skip, order_by
        )

    def get_inference_results(
        self,
        device_id: str,
        filter: str = None,
        number_of_inference_results: int = None,
        raw: int = None,
        time: str = None,
    ):
        """Abstract function call to ``get_inference_results`` API

        Args:
            device_id (str, required) : The Device ID.
            filter (str, optional) : The Filter. Search filter (same specifications as Cosmos DB UI
                                     on Azure portal except for the following)

                                        - No need to prepend where string
                                        - It is not necessary to add a deviceID.

            number_of_inference_results (int, optional) :Number of acquisitions.
                                                         If not specified: 20

            raw (int, optional) : The Raw. Data format of inference results.
                                    - 1:Append records stored in Cosmos DB.
                                    - 0:Not granted.

                                        If not specified: 0

            time (str, optional) : The Time. Inference result data stored in Cosmos DB.
                                   yyyyMMddHHmmssfff
                                    - yyyy: 4-digit year string
                                    - MM: 2-digit month string
                                    - dd: 2-digit day string
                                    - HH: 2-digit hour string
                                    - mm: 2-digit minute string
                                    - ss: 2-digit seconds string
                                    - fff: 3-digit millisecond string

        Returns:
            dict: Dictionary object returned by ``get_inference_results`` API
        """
        return self._get_inference_results_obj.get_inference_results(
            device_id, filter, number_of_inference_results, raw, time
        )
