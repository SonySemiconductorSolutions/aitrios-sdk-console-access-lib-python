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
# pylint:disable=too-many-lines
# pylint:disable=wrong-import-position
# pylint:disable=broad-except
# pylint:disable=logging-fstring-interpolation
# pylint:disable=too-many-instance-attributes
# pylint:disable=too-many-public-methods
# pylint:disable=too-many-statements
# pylint:disable=no-else-return
# pylint:disable=too-many-branches
# pylint:disable=duplicate-code

import os
import sys
import time
import warnings

import streamlit as st
import yaml

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.client import Client


class ConsoleAccessLibraryUIDemo:
    """Class to access Console APIs using Streamlit Demo App"""

    def __init__(self):
        """Constructor Method for ConsoleAccessLibraryUIDemo
        Args:
            app_config_file_path (str): File path for APP configuration
            demo_config_file_path (str): FIle path for demo configuration
        """

        st.set_page_config(page_title="Home", page_icon="👋")
        st.sidebar.write("### Console Access Library! 👋")
        self._apply_custom_css_styles_to_streamlit_widgets()
        self.console_access_settings_file_path = None
        self.demo_config_file_path = None
        self.load_ui_flag = False

        self._uploaded_files = st.file_uploader(
            "Choose Configuration files:", accept_multiple_files=True
        )
        if self._uploaded_files:
            for _uploaded_file in self._uploaded_files:
                self._save_uploadedfile(_uploaded_file)

            if os.path.exists(self.console_access_settings_file_path) and os.path.exists(
                self.demo_config_file_path
            ):
                try:
                    # Read the Configuration File
                    with open(self.demo_config_file_path, "r", encoding="utf-8") as file:
                        self._demo_configuration = yaml.safe_load(file)

                        self.load_ui_flag = True
                        # self._init_global_variables()
                        self._client_obj = Client(self.console_access_settings_file_path)

                        # Store yaml configuration
                        self.device_id = self._demo_configuration["demo_configuration"]["device_id"]
                        self.skip = self._demo_configuration["demo_configuration"]["skip"]
                        self.number_of_images = self._demo_configuration["demo_configuration"][
                            "number_of_images"
                        ]
                        self.sub_directory_name = self._demo_configuration["demo_configuration"][
                            "sub_directory_name"
                        ]
                        self.filter = self._demo_configuration["demo_configuration"]["filter"]
                        self.number_of_inferenceresults = self._demo_configuration[
                            "demo_configuration"
                        ]["number_of_inferenceresults"]
                        self.raw = self._demo_configuration["demo_configuration"]["raw"]
                        self.time = self._demo_configuration["demo_configuration"]["time"]
                        self.get_images_order_by = self._demo_configuration["demo_configuration"][
                            "get_images_order_by"
                        ]

                except KeyError as err:
                    st.error(str(err))

            else:
                st.error(
                    'Load both "console_access_settings.yaml" and "demo_config.yaml" configuration'
                    " files"
                )
        else:
            st.error("Configuration files not uploaded!!")

    def _apply_custom_css_styles_to_streamlit_widgets(self):
        """Function to customize css style for streamlit app page."""

        # Update css styling for streamlit.text_input
        st.sidebar.markdown(
            """
            <style>
            .stTextInput>div>div>input {
                font-family: "Open Sans", sans-serif;
                font-size: 16px;
                height: 35px;
            }
            .stTextInput>label{
                font-family: "Open Sans", sans-serif;
                font-size: 16px;
                letter-spacing: 1px;
                text-decoration: none;
                color: #273346;
                align-items: stretch;
                position: relative;
            }
            div.row-widget.stTextInput > div[data-baseweb="input"]{
                border: 2px solid;
                border-radius: 0.25em;
                padding: 0.25em 0.5em;
                align-items: stretch;
                position: relative;
            }
            .stSelectbox>label{
                font-family: "Open Sans", sans-serif;
                font-size: 16px;
                letter-spacing: 1px;
                text-decoration: none;
                color: #273346;
                align-items: stretch;
                position: relative;
                padding-bottom: 10px;
            }
            div.row-widget.stSelectbox > div[data-baseweb="select"]{
                cursor: pointer;
                border: 1px solid;
                border-radius: 0.25em;
                padding: 0.25em 0.25em;
                align-items: stretch;
                position: relative;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # Update sidebar border color and thickness using css styling
        st.sidebar.markdown(
            """
        <style>
        section[data-testid="stSidebar"]{
            color: CadetBlue;
            background-color:#ADD8E6;
            border: 3px solid;
        }
        </style>""",
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <style>
        .stButton>button {
            font-family: "Open Sans", sans-serif;
            font-size: 14px;
            letter-spacing: 2px;
            text-decoration: none;
            color: #273346;
            cursor: pointer;
            border: 1px solid;
            padding: 0.25em 0.5em;
            position: relative;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
        }
        .stButton>button:active {
            box-shadow: 0px 0px 0px 0px;
            top: 5px;
            left: 5px;
        }
        @media (min-width: 768px) {
            .stButton>button {
                padding: 0.25em 0.75em;
            }
        }
        </style>""",
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <style>
        div.row-widget.stCheckbox > label[data-baseweb="checkbox"]{
            font-family: "Open Sans", sans-serif;
            font-size: 12px;
            letter-spacing: 1px;
            text-decoration: none;
            color: #273346;
            cursor: pointer;
            border: 1px solid;
            padding: 0.25em 0.5em;
            box-shadow: 1px 1px 0px 0px, 1px 1px 0px 0px, 2px 2px 0px 0px,
                        3px 3px 0px 0px, 2px 2px 0px 0px;
            position: relative;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
        }
        </style>""",
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <style>
        div[data-testid="stForm"]{
            color: #d33682;
            border: 1px solid;
            padding: 2.0em 2.0em 2.0em 2.0em;
            box-shadow: 1px 1px 0px 0px, 1px 1px 0px 0px, 2px 2px 0px 0px,
                        3px 3px 0px 0px, 2px 2px 0px 0px;
            position: relative;
            user-select: none;
            -webkit-user-select: none;
        }
        </style>""",
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <style>
        div[data-testid="stMarkdownContainer"]>h3{
            font-family: "Open Sans", sans-serif;
            letter-spacing: 1px;
            text-decoration: none;
            text-transform: uppercase;
            color: #273346;
            cursor: pointer;
            padding: 0.25em 0.5em;
            position: relative;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
        }
        </style>""",
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <style>
        div[data-testid="stFileUploader"]>label{
            font-family: "Open Sans", sans-serif;
            font-size: 18px;
            letter-spacing: 1px;
            text-decoration: none;
            text-transform: uppercase;
            color: #d33682;
            cursor: pointer;
            padding: 0.5em 0.5em;
            position: relative;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
        }
        div[data-testid="stFileUploader"]{
            font-family: "Open Sans", sans-serif;
            letter-spacing: 1px;
            text-decoration: none;
            color: #d33682;
            border: 1px solid;
            padding: 2.0em 2.0em 2.0em 2.0em;
            box-shadow: 1px 1px 0px 0px, 1px 1px 0px 0px, 2px 2px 0px 0px,
                        3px 3px 0px 0px, 2px 2px 0px 0px;
            position: relative;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
        }
        div[data-testid="stFileUploader"]>section>button{
            font-family: "Open Sans", sans-serif;
            letter-spacing: 1px;
            text-decoration: none;
            color: #d33682;
            border: 1px solid;
            padding: 0.5em 0.5em 0.5em 0.5em;
            box-shadow: 1px 1px 0px 0px, 1px 1px 0px 0px, 2px 2px 0px 0px,
                        3px 3px 0px 0px, 2px 2px 0px 0px;
            position: relative;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
        }
        </style>""",
            unsafe_allow_html=True,
        )

    def _save_uploadedfile(self, uploadedfile):
        """Function to save files uploaded by user in streamlit app.

        Args:
            uploadedfile (file): files uploaded for app and demo config

        Returns:
            str: Success message if file is saved successfully.
        """
        _config_saved_dir = os.getcwd()
        if uploadedfile.name == "console_access_settings.yaml":
            self.console_access_settings_file_path = os.path.join(
                _config_saved_dir, "samples", "console_access_settings.yaml"
            )
            with open(self.console_access_settings_file_path, "wb") as file:
                file.write(uploadedfile.getbuffer())

        if uploadedfile.name == "demo_config.yaml":
            self.demo_config_file_path = os.path.join(
                _config_saved_dir, "samples", "demo_config.yaml"
            )
            with open(self.demo_config_file_path, "wb") as file:
                file.write(uploadedfile.getbuffer())

        return st.success(f"Saved File:{uploadedfile.name} to { _config_saved_dir}")

    def _print_logs(self, container, message, output_json):
        """Function to print logs on UI for all APIs
        Args:
            container (object): streamlit container object
            message (str): Message to be displayed in streamlit App.
            output_json (json): json response from APIs that is to be printed.
        """
        message = f"Result of API : {message}"
        container.write(message)
        container.write(output_json)

    def verify_get_devices(self):
        """Function to verify get_devices API in demo app"""

        _checkbox_verify_get_devices = st.sidebar.checkbox(" 1. Get Devices ")
        with st.form("form_verify_get_devices", clear_on_submit=False):
            if _checkbox_verify_get_devices:

                # Every form must have a submit button.
                _submitted = st.form_submit_button("Get Devices")
                if _submitted:
                    with st.spinner():
                        time.sleep(0.5)
                        try:
                            _output_get_devices = (
                                self._client_obj.device_management.get_devices()
                            )
                            self._print_logs(st, "get_devices", _output_get_devices)
                            st.success("Successfully Completed!")
                        except Exception as ex:
                            st.error("Internal Error occurred during API call", ex)

    def verify_start_upload_inference_result(self):
        """Function to verify start_upload_inference_result API in demo app"""

        _checkbox_verify_start_upload_inference_result = st.sidebar.checkbox(
            " 2. Start Upload Inference Result "
        )
        with st.form("form_verify_start_upload_inference_result", clear_on_submit=False):
            if _checkbox_verify_start_upload_inference_result:

                # Every form must have a submit button.
                _submitted = st.form_submit_button("Start Upload Inference Result")
                if _submitted:
                    with st.spinner():
                        time.sleep(0.5)
                        try:
                            _output_start_upload_inference_result = (
                                self._client_obj.device_management.
                                start_upload_inference_result(self.device_id)
                            )
                            self._print_logs(
                                st,
                                "_output_start_upload_inference_result",
                                _output_start_upload_inference_result,
                            )
                            st.success("Successfully Completed!")
                        except Exception as ex:
                            st.error("Internal Error occurred during API call", ex)

    def verify_stop_upload_inference_result(self):
        """Function to verify stop_upload_inference_result API in demo app"""

        _checkbox_verify_stop_upload_inference_result = st.sidebar.checkbox(
            " 3. Stop Upload Inference Result "
        )
        with st.form("form_verify_stop_upload_inference_result", clear_on_submit=False):
            if _checkbox_verify_stop_upload_inference_result:

                # Every form must have a submit button.
                _submitted = st.form_submit_button("Stop Upload Inference Result")
                if _submitted:
                    with st.spinner():
                        time.sleep(0.5)
                        try:
                            _output_stop_upload_inference_result = (
                                self._client_obj.device_management.stop_upload_inference_result(
                                    self.device_id
                                )
                            )
                            self._print_logs(
                                st,
                                "stop_upload_inference_result",
                                _output_stop_upload_inference_result,
                            )
                            st.success("Successfully Completed!")
                        except Exception as ex:
                            st.error("Internal Error occurred during API call", ex)

    def verify_get_command_parameter_file(self):
        """Function to verify get_command_parameter_file API in demo app"""

        _checkbox_verify_get_command_parameter_file = st.sidebar.checkbox(
            " 4. Get Command Parameter File "
        )
        with st.form("form_verify_get_command_parameter_file", clear_on_submit=False):
            if _checkbox_verify_get_command_parameter_file:

                # Every form must have a submit button.
                _submitted = st.form_submit_button("Get Command Parameter File")
                if _submitted:
                    with st.spinner():
                        time.sleep(0.5)
                        try:
                            _output_get_command_parameter_file = (
                                self._client_obj.device_management.get_command_parameter_file()
                            )
                            self._print_logs(
                                st, "get_command_parameter_file", _output_get_command_parameter_file
                            )
                            st.success("Successfully Completed!")
                        except Exception as ex:
                            st.error("Internal Error occurred during API call", ex)

    def verify_get_image_directories(self):
        """Function to verify get_image_directories API in demo app"""

        _checkbox_verify_get_image_directories = st.sidebar.checkbox(" 5. Get Image Directories ")
        with st.form("form_verify_get_image_directories", clear_on_submit=False):
            if _checkbox_verify_get_image_directories:

                # Every form must have a submit button.
                _submitted = st.form_submit_button("Get Image Directories")
                if _submitted:
                    with st.spinner():
                        time.sleep(0.5)
                        try:
                            _output_get_image_directories = (
                                self._client_obj.insight.get_image_directories(self.device_id)
                            )
                            self._print_logs(
                                st, "get_image_directories", _output_get_image_directories
                            )
                            st.success("Successfully Completed!")
                        except Exception as ex:
                            st.error("Internal Error occurred during API call", ex)

    def verify_get_images(self):
        """Function to verify get_images API in demo app"""

        _checkbox_verify_get_images = st.sidebar.checkbox(" 6. Get Images ")
        with st.form("form_verify_get_images", clear_on_submit=False):
            if _checkbox_verify_get_images:

                # Every form must have a submit button.
                _submitted = st.form_submit_button("Get Images")
                if _submitted:
                    with st.spinner():
                        time.sleep(0.5)
                        try:
                            _output_get_images = self._client_obj.insight.get_images(
                                self.device_id, self.sub_directory_name
                            )
                            self._print_logs(st, "get_images", _output_get_images)
                            st.success("Successfully Completed!")
                        except Exception as ex:
                            st.error("Internal Error occurred during API call", ex)

    def verify_get_inference_results(self):
        """Function to verify get_inference_results API in demo app"""

        _checkbox_verify_get_inference_results = st.sidebar.checkbox(" 7. Get Inference Results ")
        with st.form("form_verify_get_inference_results", clear_on_submit=False):
            if _checkbox_verify_get_inference_results:

                # Every form must have a submit button.
                _submitted = st.form_submit_button("Get Inference Results")
                if _submitted:
                    with st.spinner():
                        time.sleep(0.5)
                        try:
                            _output_get_inference_results = (
                                self._client_obj.insight.get_inference_results(self.device_id)
                            )
                            self._print_logs(
                                st, "get_inference_results", _output_get_inference_results
                            )
                            st.success("Successfully Completed!")
                        except Exception as ex:
                            st.error("Internal Error occurred during API call", ex)


if __name__ == "__main__":
    console_lib_ui_demo = ConsoleAccessLibraryUIDemo()

    # pylint:disable=invalid-name
    load_ui_flag = console_lib_ui_demo.load_ui_flag
    if load_ui_flag:
        console_lib_ui_demo.verify_get_devices()
        console_lib_ui_demo.verify_start_upload_inference_result()
        console_lib_ui_demo.verify_stop_upload_inference_result()
        console_lib_ui_demo.verify_get_command_parameter_file()
        console_lib_ui_demo.verify_get_image_directories()
        console_lib_ui_demo.verify_get_images()
        console_lib_ui_demo.verify_get_inference_results()
