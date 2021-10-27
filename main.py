import boto3
import random
import os
from dotenv import load_dotenv

load_dotenv()
cluster=os.environ.get("CLUSTER_NAME")
region=os.environ.get("REGION")
ecs = boto3.client("ecs", region_name=region)

def lambda_handler():
    response = ecs.list_services(
        cluster=cluster,
        )
    services = response["serviceArns"]
    return services

def describe_services():
    response = ecs.delete_service(
        cluster=cluster,
        service=random.choice(lambda_handler())
    )
    print(response)


describe_services()
