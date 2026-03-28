import boto3

def list_ec2_instances():
    ec2 = boto3.client('ec2', region_name='us-east-1')

    response = ec2.describe_instances()

    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance['InstanceId'])

    return instances


def start_instance(instance_id):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    ec2.start_instances(InstanceIds=[instance_id])
    print(f"Started instance: {instance_id}")


if __name__ == "__main__":
    print("Fetching EC2 instances...")
    instances = list_ec2_instances()

    print("Instances:", instances)

    if instances:
        start_instance(instances[0])
