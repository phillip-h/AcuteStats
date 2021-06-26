import boto3
from datetime import datetime

from fetch import get_stats

def write_stats_to_dynamo(spigot_id, bstats_id, table):
    """
    Fetch stats for the plugin with the given Spigot ID and/or
    bStats ID and store the result in the given DynamoDB table.

    It is assumed that the table is keyed by a string field
    "timestamp", this field will be set to the current time.

    See get_stats for more information.
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table)
    
    stats = get_stats(spigot_id, bstats_id)
    stats['timestamp'] = str(datetime.now())
    table.put_item(Item=stats)
