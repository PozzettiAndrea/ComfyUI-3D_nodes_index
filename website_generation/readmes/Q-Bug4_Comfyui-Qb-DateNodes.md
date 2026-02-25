# NowFormatterNode

A custom node designed for ComfyUI, allowing users to format the current date and time based on a specified format.

[中文说明 (README-CN.md)](README-CN.md)

## Overview

The `NowFormatterNode` class provides a way to obtain the current date and time in a customizable format. Users can specify the format pattern, which will be converted to the `strftime` format to produce a formatted string of the current date and time.

## Usage

### Inputs

- `format` (string): The desired format of the date and time. Default is `"yyyy-MM-dd-hhmmss"`.
    - Use the following symbols:
        - `yyyy`: Full year (e.g., 2024)
        - `YY`: 2-digit year (e.g., 24)
        - `MM`: Month (01 to 12)
        - `dd`: Day of the month (01 to 31)
        - `hh`: Hour in 24-hour format (00 to 23)
        - `mm`: Minutes (00 to 59)
        - `ss`: Seconds (00 to 59)

### Output

- `formatted_datetime` (string): The current date and time, formatted according to the specified input pattern.

## Example

To format the current date and time as `"2024-11-03-142530"`:
1. Set `format` to `"yyyy-MM-dd-hhmmss"`.
2. The output will be formatted based on the current date and time.

## Code Structure

The node uses the `strftime` function to generate the formatted date and time. Any errors in format specification will raise a `ValueError` with a detailed message.

## Development

### Class Structure

- **`INPUT_TYPES`**: Specifies the `format` input.
- **`RETURN_TYPES` and `RETURN_NAMES`**: Define the output type and name as `formatted_datetime`.
- **`format_datetime` Method**: Main function that formats the date and time.
- **`IS_CHANGED` Method**: Placeholder, returning NaN to indicate this node has no state that would trigger a change on its own.

## Error Handling

If the `format` pattern is invalid, a `ValueError` will be raised to indicate the issue.

For the Chinese version, please refer to the [中文说明 (README-CN.md)](README-CN.md).

---

