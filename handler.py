import boto3
import random
import json


cluster="some_cluster"
region="some_region"
ecs = boto3.client("ecs", region_name=region)


def list_services():
    response = ecs.list_services(
        cluster=cluster,
        )
    services = response["serviceArns"]
    return services

def delete_random_service(event, context):
    response = ecs.delete_service(
        cluster=cluster,
        service=random.choice(list_services())
    )
    print("chaos monkey randomly removed one of the services in " + json.dumps(response['service']['clusterArn']) + " and that service was a " + json.dumps(response['service']['serviceName'], indent=4, sort_keys=True, default=str))
