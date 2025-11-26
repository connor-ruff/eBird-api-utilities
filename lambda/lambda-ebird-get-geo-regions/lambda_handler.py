import json 
from utils import *

def lambda_handler(event, context):
    
    payload = json.loads(event["body"])["data"][0]
    region_type = payload[1]
    region_code = payload[2]

    api_creds_obj = get_api_creds()
    ebird_api_key = api_creds_obj['api_key']

    response_json = list_subregions(ebird_api_key, region_type, region_code)
    drop_file_in_s3(
        data=response_json,
        bucket_name=EBIRD_BASE_BUCKET,
        file_key=f'{EBIRD_BASE_BUCKET_SUBFOLDER}/geo_regions/{region_type}/{region_code}.json'
    )

    return {
        "statusCode": 200,
        "body": json.dumps({

            "data": [
               [0, "SUCCESS"]
            ]
        })
    }