# ComfyUI Google Sheets Integration

This custom node allows integration between ComfyUI and Google Sheets, enabling reading from and writing to Google Sheets directly from ComfyUI workflows.

## Installation

1. Clone this repository into the `custom_nodes` directory of your ComfyUI installation:
   ```bash
   git clone https://github.com/lazniak/comfyui-google-sheets-integration.git
   ```

2. Install the required dependencies:
   ```bash
   pip install google-auth-oauthlib>=0.4.6 google-auth-httplib2>=0.1.0 google-api-python-client>=2.0.0 cryptography>=36.0.0
   ```

## Getting client_secret.json

To use this node, you need to set up Google Sheets API and obtain the `client_secret.json` file. Here's how:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google Sheets API:
   - In the sidebar, click on "APIs & Services" > "Library"
   - Search for "Google Sheets API"
   - Click on it and press "Enable"
4. Set up credentials:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth client ID"
   - Choose "Desktop app" as application type
   - Give it a name (e.g., "ComfyUI Google Sheets Integration")
   - Click "Create"
5. Download the credentials:
   - Find your created OAuth 2.0 Client ID in the list
   - Click the download icon (⬇️) on the right
   - This will download your `client_secret.json` file
6. Place the downloaded `client_secret.json` file in the `comfyui_google_sheets_integration` directory

**First-time setup note**: When you first use the nodes, a browser window will open asking you to authorize the application. Follow the prompts to grant access to your Google Sheets.

## Usage

### Google Sheets Reader Node

This node allows you to read data from a Google Sheets spreadsheet.

Inputs:
- `spreadsheet_id`: The ID of the Google Sheets spreadsheet (found in the URL: docs.google.com/spreadsheets/d/**spreadsheet_id**/edit)
- `range`: The range of cells to read (e.g., "Sheet1!A1:B10")
- `client_secrets_file`: Path to your `client_secret.json` file (default path should work if you followed installation instructions)

Output:
- A list of strings, where each string represents a row from the spreadsheet

### Google Sheets Writer Node

This node allows you to write data to a Google Sheets spreadsheet.

Inputs:
- `spreadsheet_id`: The ID of the Google Sheets spreadsheet
- `range`: Sheet name and column to append data (e.g., "Sheet1!A")
- `client_secrets_file`: Path to your `client_secret.json` file
- `STORE`: The data to be written as a string

Output:
- A confirmation message indicating success or error details

## Use Cases

1. **Training Data Management**:
   - Track and log your model training sessions
   - Record prompt parameters and their results
   - Save image generation settings for later reference
   - Keep track of successful vs unsuccessful generations

2. **Workflow Automation**:
   - Read prompts from a spreadsheet for batch processing
   - Save generation metadata for multiple images
   - Log error messages and debugging information
   - Track resource usage and processing times

3. **A/B Testing and Experimentation**:
   - Record different prompt variations and their outcomes
   - Track model performance across different settings
   - Save comparison results between different workflows
   - Log user feedback and ratings

4. **Collaborative Projects**:
   - Share generation parameters with team members
   - Collect and aggregate feedback from multiple users
   - Track project progress and milestones
   - Share and version control prompts

5. **Dataset Creation and Management**:
   - Log dataset creation parameters
   - Track image attributes and metadata
   - Record dataset cleaning and preprocessing steps
   - Manage dataset versions and modifications

6. **Quality Control and Monitoring**:
   - Track successful vs failed generations
   - Log error rates and types
   - Monitor system performance over time
   - Record user feedback and quality ratings

7. **Research and Analysis**:
   - Log experimental results
   - Track parameter optimization results
   - Record comparative analysis data
   - Save statistical measurements and metrics

8. **Production Workflow Management**:
   - Track batch processing jobs
   - Log production metrics
   - Monitor resource utilization
   - Record completion times and success rates

## Notes

- Ensure that your Google Sheets API credentials have the necessary permissions for reading and writing
- Keep your `client_secret.json` file secure and never share it publicly
- The first time you use these nodes, you'll need to authorize the application in your web browser
- Each write operation appends data to the first empty cell in the specified column

## Troubleshooting

If you encounter any issues:

1. Check the `google_sheets_plugin.log` file in the plugin directory for detailed error messages
2. Ensure your Google Sheets API is enabled and credentials are properly set up
3. Verify that your spreadsheet ID and range are correct
4. Check if you have proper permissions for the spreadsheet
5. Make sure you're connected to the internet

For API-related errors:
- Check if you've completed the OAuth authorization process
- Verify that your API credentials haven't expired
- Ensure your Google Cloud project has the Sheets API enabled
- Check if you've exceeded API quotas

## License

This project is licensed under Apache 2.0 lic. - see the LICENSE file for details.
