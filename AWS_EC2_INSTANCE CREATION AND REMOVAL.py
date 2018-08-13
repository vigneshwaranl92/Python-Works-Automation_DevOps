import boto3
import awscli


"""
Created by : Vigneshwaran Loganathan
Date : 13/08/2018
Purpose : Get to Know about EC2 creation through AWSCLI(Amazon Web Services Command Line Interface)

"""
"""
Boto is the Amazon Web Services (AWS) SDK for Python, 
which allows Python developers to write software that makes use of Amazon services like S3 and EC2. 
Boto provides an easy to use, object-oriented API as well as low-level direct service access
"""

"""
AWSCLI is the command line interface for accessing AWS management console
To access a AWASCLI in any terminal, type the below in the prompt 
>>"aws configure"   # This will initialise the configuration of AWSCLI
AWS Access Key ID [None]:         #To get the access key, goto AWS Management Console 
AWS Secret Access Key [None]:     #Under >services>IAM(Identity and Access Management), create a new user
Default region name [None]:       #Once user created, download a copy of CSV format and store it in the local drive
Default output format [None]:     #as it cannot be viewed again 
"""
"""
The below program will create EC2 instance and provide the Instance ID
Once after the instance id is obtained it will delete the created instance
(As it is for test purpose)
"""

EC2 = boto3.resource('ec2')  #creating an object for ec2(elastic cloud compute)
                             # hence it can be called back with the name EC2

Instance = EC2.create_instances(
    ImageId='ami-8c122be9',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro')   #Defining the parameters for EC2 Instance creation
print(Instance[0].id)
Instance_Id = Instance[0].id
#Process for Deletion
instance=EC2.Instance(Instance_Id)
response = instance.terminate()
print(response)




