#!/usr/bin/python
import boto3
session=boto3.session.Session(profile_name="vineet848531")
ec2_con_re=session.resource(service_name="ec2",region_name="ap-south-1")
my_inst=ec2_con_re.Instance(id="i-04d79d94e0415e891")
#print dir(my_inst)
my_inst.start()
#my_inst.stop()
