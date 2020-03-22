# python
Python estructure for exercises and documentation


## AWS SDK for Python (boto3)

### Boto3 Docs Documentation
[AWS Lambda Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html)

### AWS Documentation
[AWS SDK para Python (Boto3)](https://aws.amazon.com/es/sdk-for-python/)
*example*
```
for i in ec2.instances.all():
    if i.state['Name'] == 'stopped':
        i.start()
```
### Blog Unipython
[Blog Boto3](https://unipython.com/aws-sdk-para-python-boto3/)




