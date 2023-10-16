```python
import boto3

def deploy_to_aws():
    # Create an EC2 resource object using AWS SDK
    ec2 = boto3.resource('ec2')

    # Create a new EC2 instance
    instance = ec2.create_instances(
        ImageId='ami-0abcdef1234567890',  # Replace with your image id
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='your-key-pair',  # Replace with your key pair name
        SubnetId='subnet-0abcdef1234567890'  # Replace with your subnet id
    )

    print("Deployed EC2 Instance ID:", instance[0].id)

if __name__ == "__main__":
    deploy_to_aws()
```