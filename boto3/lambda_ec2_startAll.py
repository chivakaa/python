import os
import boto3

for i in ec2.instances.all():
    if i.state['Name'] == 'stopped':
        i.start()
        print("Instance started: ", instance[0].id)
