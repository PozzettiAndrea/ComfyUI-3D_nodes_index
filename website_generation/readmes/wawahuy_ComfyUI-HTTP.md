# ComfyUI-HTTP

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Maintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/wawahuy/ComfyUI-HTTP/graphs/commit-activity)

![alt text](sample-workflow/wf.png)

**Professional HTTP integration nodes for ComfyUI workflows** - Transform your ComfyUI experience with seamless web API connectivity, enabling powerful automation and data exchange capabilities.

## Features

- **Complete HTTP Methods**: GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS
- **Session Management**: Persistent sessions with cookies and authentication
- **Authentication Support**: Basic, Bearer, API Key, Token, OAuth2
- **Form Data Handling**: Text fields, file uploads, image uploads, multipart forms
- **JSON Processing**: Parse, format, extract fields with JSONPath support
- **Image Operations**: Load images from URLs, convert to/from base64
- **File Operations**: Upload files of any type with automatic content-type detection
- **Utilities**: URL encoding, timestamps, signatures, and more
- **Error Handling**: Robust error handling with retry logic
- **Proxy Support**: HTTP/HTTPS proxy configuration

### Installation

#### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "ComfyUI-HTTP"
3. Click Install

#### Method 2: Manual Installation
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/wawahuy/ComfyUI-HTTP.git
cd ComfyUI-HTTP
pip install -r requirements.txt
```

## Node Categories

### HTTP/Session
- **HTTP Session Manager**: Create and manage persistent HTTP sessions
- **HTTP Authentication**: Configure various authentication methods

### HTTP/Methods
- **HTTP GET Request**: Perform GET requests with full configuration
- **HTTP POST Request**: POST with JSON, form data, or raw data support
- **HTTP PUT Request**: PUT requests for updates
- **HTTP PATCH Request**: PATCH requests for partial updates  
- **HTTP DELETE Request**: DELETE requests
- **HTTP HEAD Request**: HEAD requests to get headers only
- **HTTP OPTIONS Request**: OPTIONS requests for CORS and allowed methods

### HTTP/Form Data
- **HTTP Form Data**: Container for multipart form data
- **HTTP Form Data Item**: Basic form field
- **HTTP Form Text Item**: Text form field with content type
- **HTTP Form File Item**: File upload field
- **HTTP Form Image Item**: Image upload field (from ComfyUI IMAGE)
- **HTTP Form Data Concat**: Combine multiple form data objects

### HTTP/JSON
- **HTTP Convert JSON**: Parse, format, stringify, minify JSON
- **HTTP Get JSON Field**: Extract fields using JSONPath or simple notation

### HTTP/File Operations
- **HTTP File Upload**: Upload files with progress and configuration

### HTTP/Image Operations
- **HTTP Image Loader**: Load images from URLs with resizing options

### HTTP/Image Conversion
- **Base64 to Image**: Convert base64 strings to ComfyUI IMAGE
- **Image to Base64**: Convert ComfyUI IMAGE to base64 strings

### HTTP/Display
- **HTTP Display Result**: Format and display HTTP responses

### HTTP/Utilities
- **HTTP Utils**: Various utility functions (URL encoding, signatures, etc.)

## Usage Examples

### Basic GET Request

```
[HTTP GET Request]
url: "https://api.github.com/users/octocat"
↓
status_code: 200
headers: {...}
content: {"login": "octocat", ...}
json: (formatted JSON)
```

### POST with JSON Data

```
[HTTP POST Request]
url: "https://api.example.com/users"
content_type: "json"
json_data: '{"name": "John", "email": "john@example.com"}'
↓
status_code: 201
content: {"id": 123, "name": "John", ...}
```

### Session with Authentication

```
[HTTP Session Manager]
session_name: "api_session"
base_url: "https://api.example.com"
auth_type: "bearer"
token: "your_token_here"
↓
session → [HTTP GET Request]
           url: "/users/me"
```

### Form Data with File Upload

```
[HTTP Form File Item]          [HTTP Form Text Item]
name: "document"               name: "title" 
file_path: "/path/to/file.pdf" value: "My Document"
↓                              ↓
form_item                      form_item
         ↓                ↓
      [HTTP Form Data]
      ↓
      form_data → [HTTP POST Request]
                  content_type: "form-data"
```

### Image Upload from ComfyUI

```
[Load Image] → [HTTP Form Image Item]
               name: "photo"
               format: "JPEG"
               quality: 95
               ↓
               form_item → [HTTP Form Data] → [HTTP POST Request]
```

### Load Image from URL

```
[HTTP Image Loader]
url: "https://example.com/image.jpg"
resize_mode: "fit" 
target_width: 512
target_height: 512
↓
image (ComfyUI IMAGE tensor)
```

### JSON Field Extraction

```
[HTTP GET Request] → [HTTP Get JSON Field]
                     field_path: "$.data.users[0].name"
                     extraction_method: "jsonpath"
                     ↓
                     value: "John Doe"
```

## Authentication Methods

### Basic Authentication
```json
{
  "auth_type": "basic",
  "username": "your_username", 
  "password": "your_password"
}
```

### Bearer Token
```json
{
  "auth_type": "bearer",
  "token": "your_bearer_token"
}
```

### API Key
```json
{
  "auth_type": "api_key",
  "api_key": "your_api_key",
  "api_key_header": "X-API-Key"
}
```

### Custom Headers
```json
{
  "auth_type": "none",
  "custom_headers": "{\"Authorization\": \"Custom your_token\"}"
}
```

## Session Management

Sessions maintain:
- Cookies across requests
- Authentication credentials
- Custom headers
- Connection pooling
- Base URL for relative requests

```
[HTTP Session Manager] → [Multiple HTTP Requests]
```

## Error Handling

All nodes include robust error handling:
- Network timeouts with retries
- SSL verification options
- Proxy support
- Detailed error messages
- Graceful fallbacks

## JSONPath Support

Extract data from JSON responses using JSONPath expressions:

- `$.data` - Root data field
- `$.users[0].name` - First user's name
- `$.users[*].email` - All user emails
- `$..price` - All price fields recursively

## Utility Functions

The HTTP Utils node provides:
- URL encoding/decoding
- Base64 encoding/decoding  
- JSON escaping/unescaping
- HTML escaping/unescaping
- Timestamp generation
- UUID generation
- HMAC signature generation
- URL parsing and building
- Email validation
- Authentication header creation

## Best Practices

1. **Use Sessions**: For multiple requests to the same API, use HTTP Session Manager
2. **Handle Errors**: Always check status codes and use HTTP Display Result
3. **Secure Credentials**: Use environment variables for sensitive data
4. **Timeout Configuration**: Set appropriate timeouts for your use case
5. **Content Types**: Specify correct content types for better API compatibility
6. **Rate Limiting**: Implement delays between requests if needed


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **ComfyUI Team** - For creating an amazing platform for AI workflows
- **Contributors** - Thank you to all who have contributed to this project
- **Community** - For feedback, bug reports, and feature requests

## Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/wawahuy/ComfyUI-HTTP/issues)
- **GitHub Discussions**: [Ask questions or share ideas](https://github.com/wawahuy/ComfyUI-HTTP/discussions)
- **Documentation**: Check this README and code comments for usage examples

---

<div align="center">

**[Star this project](https://github.com/wawahuy/ComfyUI-HTTP/stargazers) | [Fork it](https://github.com/wawahuy/ComfyUI-HTTP/fork) | [Report Issues](https://github.com/wawahuy/ComfyUI-HTTP/issues)**

Made with love for the ComfyUI community

</div>