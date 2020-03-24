import boto3
import pandas as pd

# Define vars
ec2 = boto3.client('ec2')
response = ec2.describe_instances()


def get_ec2_status(response):
    av_zones, instance_ids, state_names= [], [], []
    for res in response['Reservations']:
        for ins in res['Instances']:
            av_zones.append(ins['Placement']['AvailabilityZone'])
            instance_ids.append(ins['InstanceId'])
            state_names.append(ins['State']['Name'])
    return pd.DataFrame({
        'InstanceId': instance_ids,
        'Availibility Zone': av_zones,
        'State': state_names
    })

data_ec2 = get_ec2_status(response)

# Stop EC2 instances
ec2.stop_instances(InstanceIds=list(data_ec2.loc[data_ec2['State'] == 'running', 'InstanceId']))

# Print EC2 status
response = ec2.describe_instances() 
data_ec2 = get_ec2_status(response) 
print(data_ec2)

