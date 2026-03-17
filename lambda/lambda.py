import boto3
import time
from datetime import datetime, timedelta

logs_client = boto3.client('logs')

LOG_GROUP_NAME = '<Log Group Name>'
S3_BUCKET = '<S3 Bucket Name>'
EXPORT_PREFIX = '<Prefix at S3>'

def lambda_handler(event, context):
    to_time = int(time.time() * 1000)
    from_time = int((datetime.utcnow() - timedelta(days=1)).timestamp() * 1000)

    task_name = f"cw-export-{int(time.time())}"

    response = logs_client.create_export_task(
        taskName=task_name,
        logGroupName=LOG_GROUP_NAME,
        fromTime=from_time,
        to=to_time,
        destination=S3_BUCKET,
        destinationPrefix=EXPORT_PREFIX
    )

    return {
        'statusCode': 200,
        'body': f"Export task created: {response['taskId']}"
    }