# Lamda_image_resize_compress
Automatically resize and compress images uploaded to an S3 bucket using an AWS Lambda function. Supports multiple formats, maintains quality, and deletes original images after processing. Easy setup and scalable. Created by Mukesh Adhikari, Xitoxito.


# Image Resizer and Compressor using AWS Lambda

This repository contains an AWS Lambda function that automatically resizes and compresses images uploaded to an S3 bucket. The function is triggered by S3 events and processes images to reduce their file size while maintaining quality. This project is designed to help developers handle image optimization seamlessly, improving website performance and reducing storage costs.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. AWS Lambda Configuration](#2-aws-lambda-configuration)
  - [3. S3 Bucket Configuration](#3-s3-bucket-configuration)
- [Usage](#usage)
- [Example](#example)
- [Code](#code)
- [License](#license)
- [Contact](#contact)

## Overview

This project aims to help developers automatically resize and compress images uploaded to an S3 bucket using an AWS Lambda function. The function reduces the image file size, making it more efficient for web use while preserving quality.

## Features

- Automatically triggered by S3 events.
- Supports multiple image formats (JPEG, PNG, etc.).
- Resizes and compresses images.
- Preserves the original image format.
- Deletes the original image after processing.
- Efficient and scalable using AWS Lambda.

## Prerequisites

- AWS Account
- Python 3.x installed
- AWS CLI configured
- Boto3 library
- Pillow library

## Setup

### 1. Clone the Repository

Clone this repository to your local machine:

```sh
git clone https://github.com/yourusername/image-resizer-compressor.git
cd image-resizer-compressor
```



2. AWS Lambda Configuration

	1.	Create a Lambda Function:
	•	Go to the AWS Lambda Console.
	•	Click on “Create function”.
	•	Choose “Author from scratch”.
	•	Name your function (e.g., ImageResizerCompressor).
	•	Choose Python 3.x as the runtime.
	•	Create a new role with basic Lambda permissions.
	2.	Configure Lambda Function:
	•	Increase memory allocation to 1024 MB or higher.
	•	Increase timeout to 5 minutes or higher.
	•	Set ephemeral storage (/tmp) to 1700 MB or higher.
	3.	Upload the Code:
	•	Copy the code from lambda_function.py in this repository.
	•	Paste it into the Lambda function code editor.
	•	Click “Deploy” to save your changes.

3. S3 Bucket Configuration

	1.	Create an S3 Bucket:
	•	Go to the S3 Console.
	•	Click on “Create bucket”.
	•	Name your bucket (e.g., xitoxito-images).
	2.	Set Up S3 Event Notification:
	•	Go to the S3 bucket properties.
	•	Click on “Events”.
	•	Add a notification to trigger the Lambda function on ObjectCreated events.

Usage

To use the image resizer and compressor, simply upload an image to your configured S3 bucket. The Lambda function will automatically process the image, resize and compress it, and then upload the processed image back to the same bucket.

Example

	1.	Upload an Image:
	•	Upload an image (e.g., example.jpg) to your S3 bucket.
	2.	Check Processed Image:
	•	After the Lambda function processes the image, the compressed image will replace the original one in the bucket.

 
