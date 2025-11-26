import requests
import boto3
import json
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo  # built into Python 3.9+
from constants import *

def get_api_creds():
    client = boto3.client('secretsmanager', region_name='us-east-2')
    secret_name = 'eBird-api-credentials'
    response = client.get_secret_value(SecretId=secret_name)
    secret_string = response['SecretString']
    return json.loads(secret_string)


def list_subregions(ebird_api_key: str, region_type: str, parent_region_code: str = "world"):
    """
    List sub-regions of given type under parent_region_code.

    region_type: "country", "subnational1", or "subnational2"
    parent_region_code: 
      - "world" for top-level country list, or
      - a valid country code (for subnational1), or
      - a valid subnational1 code (for subnational2)
    """
    headers = {
        "X-eBirdApiToken": ebird_api_key
    }
    url = f"{EBIRD_BASE_URL}/ref/region/list/{region_type}/{parent_region_code}"
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()

def drop_file_in_s3(data, bucket_name, file_key):
    s3_client = boto3.client('s3')
    s3_client.put_object(
        Body=json.dumps(data),
        Bucket=bucket_name,
        Key=file_key
    )
    print(f'File dropped in S3 at s3://{bucket_name}/{file_key}')