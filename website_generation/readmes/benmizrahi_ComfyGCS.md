# ComfyGCS

ComfyGCS is a robust read/write plugin for Google Cloud Storage, designed to simplify interaction with GCS buckets in your projects.

## Features

- Seamless integration with Google Cloud Storage.
- Easy-to-use read and write operations.
- Lightweight and efficient.


### Environment Variables

To configure ComfyGCS, set the following environment variables:

- **`GOOGLE_APPLICATION_CREDENTIALS_PATH`** (optional): Path to the Google Cloud service account key file.  
    Used for authentication when interacting with Google Cloud services. If not provided, the application will attempt to use the default credentials available in the environment.

- **`GOOGLE_PROJECT_ID`** (required): The ID of the Google Cloud project.  
    Necessary for identifying the project when making API calls to Google Cloud services.

- **`GOOGLE_BUCKET`** (required): The name of the Google Cloud Storage bucket.  
    Required for accessing or storing objects in the specified bucket.

## Requirements

- Python 3.7 or higher
- Google Cloud SDK installed and authenticated

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## Support

For issues or feature requests, please open an issue on the [GitHub repository](https://github.com/your-repo/comfygcs).
