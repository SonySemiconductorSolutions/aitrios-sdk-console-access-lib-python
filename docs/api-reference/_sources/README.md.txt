# **"Console Access Library" - Quick Start Guide**
## Steps to install "**Console Access Library**" and get started with "**Demo application**".


1. Create virtual environment
    ```
    python -m venv venv_console_access_library
    ```

2. Activate virtual environment
- Case of Linux environment:
    ```
    source venv_console_access_library/bin/activate
    ```
- Case of Windows environment:
    ```
    source venv_console_access_library/Scripts/Activate
    ```

3. Install python dependencies for "**demo application**"
    ```
    pip install -r requirements.txt
    ```

4. Install dependency python package of "**Console for AITRIOS REST Client SDK(Primitive)**" for "**Console Access Library**"
    ```
    python -m pip install lib/python-client/.
    ```

5. Install "**Console Access Library**"
    ```
    python -m pip install src/.
    ```

6. Network proxy setting

    To use the "**Console Access Library**" in a proxy environment, set the **`https_proxy`** environment variable.
    ```
    export https_proxy=http://username:password@proxyhost:port
    ```

7. To run "**Console Access Library**" sample application, set configuration parameters and edit sample application.

    * Option 1: Using console access setting configuration file

        * Step 1: Create console access setting configuration parameters with real values

            (samples\console_access_settings.yaml).

            In the case of using "**Console Developer Edition**"
            ```
            console_access_settings:
                console_endpoint: "__console_endpoint__"
                portal_authorization_endpoint: "__portal_authorization_endpoint__"
                client_secret: "__client_secret__"
                client_id: "__client_id__"
            ```

            In the case of using "**Console Enterprise Edition**"
            ```
            console_access_settings:
                console_endpoint: "__console_endpoint__"
                portal_authorization_endpoint: "__portal_authorization_endpoint__"
                client_secret: "__client_secret__"
                client_id: "__client_id__"
                application_id: "__application_id__"
            ```

        * Step 2: Import modules **`ReadConsoleAccessSettings`**, **`Config`** and **`Client`** into "**Console Access Library**" sample application 

            (samples\console_access_client_api_demo.py)
            ```
            from console_access_library.common.read_console_access_settings import ReadConsoleAccessSettings
            from console_access_library.common.config import Config
            from console_access_library.client import Client
            ```

        * Step 3: Set path for "**Console Access Library**" setting file, and then instantiate "**Console Access Library**" **`ReadConsoleAccessSettings`**.

            To create console_access_settings.yaml file, please refer step 1

            (samples\console_access_client_api_demo.py)
            ```
            SETTING_FILE_PATH = os.path.join(os.getcwd(), "samples", "console_access_settings.yaml")
            read_console_access_settings_obj = ReadConsoleAccessSettings(SETTING_FILE_PATH)
            ```

        * Step 4: Instantiate "**Console Access Library**" **`Config`**.

            (samples\console_access_client_api_demo.py)
            ```
            config_obj = Config(console_endpoint=read_console_access_settings_obj.console_endpoint, 
                                portal_authorization_endpoint=read_console_access_settings_obj.portal_authorization_endpoint, 
                                client_id=read_console_access_settings_obj.client_id, 
                                client_secret=read_console_access_settings_obj.client_secret,
                                application_id= read_console_access_settings_obj.application_id)
            ```

    * Option 2: Using Environment Variables

        * Step 1: Export the real values to environment.

            ```
            export CONSOLE_ENDPOINT="__console_endpoint__"
            export PORTAL_AUTHORIZATION_ENDPOINT="__portal_authorization_endpoint__"
            export CLIENT_SECRET="__client_secret__"
            export CLIENT_ID="__client_id__"
            export APPLICATION_ID="__application_id__"
            ```

        * Step 2: Import modules **`Config`** and **`Client`** into "**Console Access Library**" sample application 

            (samples\console_access_client_api_demo.py)
            ```
            from console_access_library.common.config import Config
            from console_access_library.client import Client
            ```

        * Step 3: Instantiate "**Console Access Library**" **`Config`**.

            (samples\console_access_client_api_demo.py)
            ```
            config_obj = Config(console_endpoint=None, 
                                portal_authorization_endpoint=None, 
                                client_id=None, 
                                client_secret=None,
                                application_id=None)
            ```

    * Option 3: Passing real values to "**Console Access Library**" **`Config`**.

        * Step 1: Import modules **`Config`** and **`Client`** into "**Console Access Library**" sample application 

            (samples\console_access_client_api_demo.py)
            ```
            from console_access_library.common.config import Config
            from console_access_library.client import Client
            ```

        * Step 2: Instantiate "**Console Access Library**" **`Config`** with real values.

            (samples\console_access_client_api_demo.py)
            ```
            config_obj = Config(console_endpoint="__console_endpoint__", 
                                portal_authorization_endpoint="__portal_authorization_endpoint__",
                                client_id="__client_id__", 
                                client_secret="__client_secret__",
                                application_id="__application_id__")
            ```

8. To run "**Console Access Library**" sample application, edit demo configuration parameters with real values.
    (samples\demo_config.yaml).
    ```
    demo_configuration:
        device_id: "__device_id__"
        get_model_device_id: "__get_model_device_id__"
        publish_model_wait_response_device_id: "__publish_model_wait_response_device_id__"
        model_id: "__model_id__"
        model: "__model__"
        converted: "__converted__"
        vendor_name: "__vendor_name__"
        comment: "__comment__"
        input_format_param: "__input_format_param__"
        network_config: "__network_config__"
        network_type: "__network_type__"
        metadata_format_id: "__metadata_format_id__"
        project_name: "__project_name__"
        model_platform: "__model_platform__"
        project_type: "__project_type__"
        latest_type: "__latest_type__"
        config_id: "__config_id__"
        sensor_loader_version_number: "__sensor_loader_version_number__"
        sensor_version_number: "__sensor_version_number__"
        model_version_number: "__model_version_number__"
        ap_fw_version_number: "__ap_fw_version_number__"
        device_ids: "__device_ids__"
        replace_model_id: "__replace_model_id__"
        timeout: "__timeout__"
        compiled_flg: "__compiled_flg__"
        app_name: "__app_name__"
        version_number: "__version_number__"
        file_name: "__file_name__"
        entry_point: "__entry_point__"
        schema_info: "__schema_info__"
        device_name: "__device_name__"
        connection_state: "__connection_state__"
        device_group_id: "__device_group_id__"
        scope: "__scope__"
        sub_directory_name: "__sub_directory_name__"
        number_of_images: "__number_of_images__"
        skip: "__skip__"
        order_by: "__order_by__"
        number_of_inference_results: "__number_of_inference_results__"
        filter: "__filter__"
        raw: "__raw__"
        time: "__time__"
    ```

9. To run API "import_device_app" in "**Console Access Library**" sample application
    ```
    Place the contents of wasm file as base64 in samples/device_app_file_content.txt
    ```

10. Run "**demo application**" using the following command
    ```
    python samples/console_access_client_api_demo.py
    ```

## Restrictions
- None

## Get support
- [Contact us](https://developer.aitrios.sony-semicon.com/en/contact-us-en)

## See also
- ["**Developer Site**"](https://developer.aitrios.sony-semicon.com/en/edge-ai-sensing/)

## Trademark
- ["**Read This First**"](https://developer.aitrios.sony-semicon.com/en/documents/read-this-first)

## Versioning

This repository aims to adhere to Semantic Versioning 2.0.0.

## Branch

See the "**Release Note**" from [**Releases**] for this repository.

Each release is generated in the main branch. Pre-releases are generated in the develop branch. Releases will not be provided by other branches.

## Security
Before using Codespaces, please read the Site Policy of GitHub and understand the usage conditions. 
