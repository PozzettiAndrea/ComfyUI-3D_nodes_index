# Comfy-UI on-complete-email-me

[한국어](./README_kr.md) | [English](/)
---
## FAQ

Q. Even after entering the app password, emails are not being sent.

A. ASCII characters may be included in the app password. Please try reapplying the app password after correcting any spaces.
(Failed to send email: 'ascii' codec can't encode character '\xa0' in position 25: ordinal not in range) <- ASCII problem

## Update (2025.01.15)

- A new feature has been added to attach the last generated image to the email.

![image](https://github.com/user-attachments/assets/427d945a-10da-41eb-9579-416952885c85)

- OnCompletePlaySound node has been added. You can now receive sound notifications upon completion.


A feature that sends an email via Gmail once image generation is completed in Comfy-ui.

# ComfyUI Notifications

- On Complete play sound node 
- On Complete Email me node
- On Complete webhook node

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation


1. Copy the Git URL
![Image 1](docs/images/install01.jpg)
2. Click on Comfy-UI-Manager
3. Click Install via GIT URL
![Image 2](docs/images/install02.jpg)
4. Paste the Git URL
5. Restart Comfy-UI

## Usage

![Image 3](docs/images/usage01.jpg)
1. Enter your Gmail email address in `sender_email`.
2. Generate and enter your Gmail app password in `sender_password` (do not enter your Gmail account password).
   - Link for creating app password: [Google App Passwords](https://myaccount.google.com/apppasswords)
3. Enter the list of recipient email addresses (separated by Enter key).
4. Enter the message to be sent.

![Image 4](docs/images/usage02.jpg)

**OnCompleteWebhook Node**

We have added a new node called OnCompleteWebhook. This node allows you to send a webhook notification upon the completion of a certain task or event.

**Usage**

1. Create the OnCompleteWebhook Node:

Follow the instructions to create the OnCompleteWebhook node in your workflow.

2. Configure the Webhook URL:

Set the webhook URL to the endpoint where you want to receive the notification.

3. Trigger the Node:

Ensure the node is triggered upon the completion of the desired task or event.
By using the OnCompleteWebhook node, you can integrate with external services and get notified about the completion of various processes.

Please update your workflows and check out the new functionality.

## License

This project is licensed under the GPL-3.0 License. See the LICENSE file for details.

