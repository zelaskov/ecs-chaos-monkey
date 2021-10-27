import boto3

def lambda_handler(event, context):
    ecs = boto3.client('ecs', region_name="eu-west-1")    
    response = ecs.list_services(
        cluster="charging-alpha-ecs-stack-ECSCluster-ra3zd0x3o98P",
        )
    print(response['serviceArns'])

lambda_handler(event="something",context="something")
