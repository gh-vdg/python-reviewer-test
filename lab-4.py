import boto3

def syncTables(event, context):
    source_ddb = boto3.client('dynamodb', 'us-east-1')
    destination_ddb = boto3.client('dynamodb', 'us-west-2')
    sync_ddb_table(source_ddb, destination_ddb)

# Scan returns paginated results, so only partial data will be copied
def sync_ddb_table(source_ddb, destination_ddb):
    response = source_ddb.scan(
        TableName="dragon_bonus_attack"
    )

   if LastEvaluateKey:
         paginator = client.get_paginator('list_objects')
   #      operation_parameters = ('TableName': 'dragon_bonus_attack')
         page_iterator = paginator.paginate(**operation_parameters)

    
    for item in response['Items']:
        destination_ddb.put_item(
            TableName="dragon_table_west",
            Item=item
        )
           
        

for page in page_iterator:
    print(page['Contents'])
        
        )
