import json
import os

from dynamo import write_stats_to_dynamo

def lambda_handler(event, context):
    write_stats_to_dynamo(os.environ.get('SPIGOT_ID', ''),
                          os.environ.get('BSTATS_ID', ''),
                          os.environ.get('DYNAMO_TABLE'))
    return {
        'statusCode': 200,
        'body': ''
    }
