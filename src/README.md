# **Console Access Library - Quick Start Guide**
Steps to install Console Access library and get started with Demo application.


1. Create virtual environment
    ```
    python -m venv venv_console_access_library
    ```

2. Activate virtual environment
    ```
    source venv_console_access_library/Scripts/Activate
    ```

3. Install python dependencies for demo application
    ```
    pip install -r requirements.txt
    ```

4. Install dependency python package of Console for AITRIOS REST Client SDK(Primitive) for Console Access Library
    ```
    python -m pip install lib/python-client/.
    ```

5. Install Console Access Library
    ```
    python -m pip install src/.
    ```

6. Set Configuration Parameter to start Console Access Library Sample Application

    * Option 1:

        Edit console access setting configuration parameters with real values(samples\console_access_settings.yaml).
        ```
        console_access_settings:
            base_url: "__base_url__"
            token_url: "__token_url__"
            client_secret: "__client_secret__"
            client_id: "__client_id__"
        ```
    * Option 2:

        Keep the default console access setting configuration parameters as null and export the real values to environment.
        (samples\console_access_settings.yaml).
        ```
        console_access_settings:
            base_url: null
            token_url: null
            client_secret: null
            client_id: null
        ```

        Export the real values to environment.
        ```
        export BASE_URL="__base_url__"
        export TOKEN_URL="__token_url__"
        export CLIENT_SECRET="__client_secret__"
        export CLIENT_ID="__client_id__"
        ```

7. To run Console Access Library sample application, edit demo configuration parameters(samples\demo_config.yaml).
    ```
    demo_configuration:
        device_id: "__device_id__"
        number_of_images: __number_of_images__
        skip: __skip__
        sub_directory_name: "__sub_directory_name__"
        number_of_inferenceresults: __number_of_inferenceresults__
        filter: "__filter__"
        raw: __raw__
        time: "__time__"
        get_images_order_by: "__get_images_order_by__"
    ```

8. Run demo application using the following command
    ```
    python samples/console_access_client_api_demo.py
    ```
