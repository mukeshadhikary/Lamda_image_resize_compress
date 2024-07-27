# lambda_function.py

import boto3
import json
from PIL import Image, UnidentifiedImageError
from io import BytesIO

s3 = boto3.client('s3')

def resize_and_compress_image(image_data, image_path, initial_quality=60):
    try:
        image = Image.open(BytesIO(image_data))
        width, height = image.size
        original_format = image.format

        # Resize and crop the image
        if height > width:
            new_size = min(width, height)
            left = (width - new_size) // 2
            top = int(height * 0.25)
            right = (width + new_size) // 2
            bottom = top + new_size
            cropped_image = image.crop((left, top, right, bottom))
        else:
            target_width = width
            target_height = int(width * 3 / 4)
            if target_height > height:
                target_height = height
                target_width = int(height * 4 / 3)
            
            left = (width - target_width) // 2
            top = (height - target_height) // 2
            right = (width + target_width) // 2
            bottom = (height + target_height) // 2
            cropped_image = image.crop((left, top, right, bottom))

        # Function to save and get size
        def save_and_get_size(image, quality):
            output_buffer = BytesIO()
            image.save(output_buffer, original_format, quality=quality)
            output_buffer.seek(0)
            return output_buffer, output_buffer.getbuffer().nbytes

        # Determine optimal quality
        low, high = 10, 95
        optimal_quality = initial_quality
        final_output_buffer = None

        while low <= high:
            mid_quality = (low + high) // 2
            output_buffer, file_size = save_and_get_size(cropped_image, mid_quality)

            if 100 * 1024 <= file_size <= 250 * 1024:
                optimal_quality = mid_quality
                final_output_buffer = output_buffer
                break
            elif file_size > 250 * 1024:
                high = mid_quality - 1
            else:
                low = mid_quality + 1

        # Save the image with optimal quality
        if final_output_buffer is None:
            final_output_buffer, file_size = save_and_get_size(cropped_image, optimal_quality)

        return final_output_buffer
    except UnidentifiedImageError:
        print(f"File is not a valid image: {image_path}")
        raise
    except Exception as e:
        print(f"Error in resize_and_compress_image: {e}")
        raise

def lambda_handler(event, context):
    print(f"Received event: {json.dumps(event)}")  # Log the entire event object
    
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        print(f"Bucket: {bucket}, Key: {key}")  # Debugging statement
        
        try:
            head_object = s3.head_object(Bucket=bucket, Key=key)
            print(f"HeadObject successful for key: {key}")
        except s3.exceptions.NoSuchKey:
            print(f"No such key: {key}")
            continue
        except s3.exceptions.ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == '404':
                print(f"Object not found: {key}")
            else:
                print(f"ClientError: {e}")
            continue
        except Exception as e:
            print(f"Unexpected error: {e}")
            continue
        
        # Check metadata to skip already compressed images
        metadata = head_object.get('Metadata', {})
        if metadata.get('is_compressed') == 'xitoxito-comp-true':
            print(f"Image {key} is already compressed. Skipping.")
            continue
        
        try:
            # Download the image from S3
            response = s3.get_object(Bucket=bucket, Key=key)
            image_data = response['Body'].read()
        except Exception as e:
            print(f"Error downloading image: {e}")
            continue

        try:
            # Resize and compress the image
            output_buffer = resize_and_compress_image(image_data, key)
        
            # Upload the processed image back to S3 with the same key
            s3.put_object(Bucket=bucket,​⬤
