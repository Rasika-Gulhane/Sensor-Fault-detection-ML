# Sensor-Fault-detection-ML 
IOT sensor streaming data from kafka to MongoDB and detecting fault using ML model within live data
Check https://github.com/Rasika-Gulhane/Sensor_Fault_Detection for data data streaming model

Dataset is taken from Scania website for heavy-duty truck's APS device that captures data:
https://www.scania.com/


### Problem Statement
The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class
indicates that the failure was caused by something else.

### Solution Proposed 
In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.

# Project Successs
1. Workflow Action continuous integration with AWS <img width="1434" alt="Workflow Action continuous integration with AWS" src="https://github.com/Rasika-Gulhane/Sensor-Fault-detection-ML/assets/67581952/e9a0e4ac-24b8-4456-be05-c3b473689418">

2. Successfully Run on EC2 server <img width="1433" alt="Successfully Run on EC2 server" src="https://github.com/Rasika-Gulhane/Sensor-Fault-detection-ML/assets/67581952/f3460894-1a51-4133-b0fe-06e9854f2491">

# AWS S3 bucket Sync API Reference

1. Login to AWS account
2. Create IAM user for deployment

    * with Specific access:
    - EC2 access: It is virtiual machine
    - S3 bucket access: To store artifact and model in s3
    - ECR : (Elastic Container Registry) : To save your Docker Image in aws

    * Description:
    - Build Docker image
    - push your docker img to ECR
    - launch your EC2
    - pull your imag from ECR to EC2
    - lauch you docker image in EC2

    Policy:
	1. AmazonEC2ContainerRegistryFullAccess
	2. AmazonEC2FullAccess
	3. AmazonS3FullAccess


3. Create a s3 bukcet in ap-south-1
	bucket name: sensor-training-model
	
4. ECR repo to store/save docker image
	367512584047.dkr.ecr.us-east-1.amazonaws.com/sensor_repo
	
5. EC2 machine  Ubuntu  Created 
    (instance created) then connect the instance

6. Open EC2 and Install docker in EC2 Machine 
	
	#optinal
	sudo apt-get update -y
	sudo apt-get upgrade
	
	#required
	curl -fsSL https://get.docker.com -o get-docker.sh
	sudo sh get-docker.sh
	sudo usermod -aG docker ubuntu
	newgrp docker
	
7. Configure EC2 as self-hosted runner

setting> actions> runner> new self hosted runner> choose your os> 
then run command one by one

8. Setup github secrets

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION=ap-south-1

AWS_ECR_LOGIN_URI=566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME=sensor-fault

MONGO_DB_URL=
