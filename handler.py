import boto3
import random
import json


cluster="cluster_name"
region="some_region"
ecs = boto3.client("ecs", region_name=region)


def list_services():
    response = ecs.list_services(
        cluster=cluster,
        )
    services = response["serviceArns"]
    return services

def delete_random_service():
    response = ecs.delete_service(
        cluster=cluster,
        service=random.choice(list_services())
    )
    print("chaos monkey randomly removed one of the services in " + json.dumps(response['service']['clusterArn']) + " and that service was a " + json.dumps(response['service']['serviceName'], indent=4, sort_keys=True, default=str))

def handler(event, context):
    delete_random_service()
