# Machine Learning Opearations (MLOps)
# Arpit Garg(ME20B035) 
# Thunguri Prajvalitha (ED20B071)

## MLOps Project

## Overview :
This project implements a robust MLOps pipeline, facilitating the continuous integration, continuous deployment, and monitoring of machine learning models. The infrastructure leverages AWS, Kubernetes, and various open-source tools to ensure scalability, reproducibility, and maintainability.



## Architecture :

![image](https://github.com/Chandru-21/MLOps_Project/assets/64595758/123511be-fe66-424d-8776-513b908840fe)

## Key Features :

**Data Versioning** : DVC

**Continuous Integration(CI)** : Triggered through ‘main.yml’ , building the code (docker), tests the code(Pytest),pushes the docker image to AWS ECR. 

**Experiment Tracking / Model Versioning** : MLflow 

**Continuous Deployment(CD)** : Deploys FastAPI in AWS EKS(kubernetes cluster) for real-time and batch predictions. 

**Continuous Monitoring(CM)** : Integrating the ‘/metrics’ method of  FastAPI in Prometheus and visualizes endpoints in Grafana.  

**Continuous Training(CT)** : Triggers code execution through GitHub Actions when new data is pushed to the remote DVC location and committed to Git. 

**Drift Monitoring** : Uses a Streamlit app to monitor data drift, target drift, and performs data quality checks.



## Model Versioning :

**ML Flow** :
![mlflow](https://github.com/user-attachments/assets/d7a2d1bd-1ee5-4298-a1d3-878828727daf)





## Data Monitoring :

**Data Drift Monitoring** :

![Screenshot 2025-05-15 183409](https://github.com/user-attachments/assets/75e772d9-7d42-4ce3-9056-d45a10771e04)




![Screenshot 2025-05-15 183419](https://github.com/user-attachments/assets/3564b36a-a3ba-4d98-88b6-2dc801ab8f85)



## Continuous Monitoring(CM)


**Exposing "/metrics" on FastAPI to be connected to Prometheus** :

![Screenshot 2025-05-15 183201](https://github.com/user-attachments/assets/cd46649e-451c-41f3-8baa-66361748dd3f)

![Screenshot 2025-05-15 183213](https://github.com/user-attachments/assets/52edbc5c-9c37-443a-8e1b-b892c71ddf8e)


![Screenshot 2025-05-15 183230](https://github.com/user-attachments/assets/5ebb79b0-72c9-436a-8709-d183f26d9f46)



**FastAPI integrated in to Prometheus** :


![promethus](https://github.com/user-attachments/assets/6cdf30fa-940f-4b8d-b6e0-744de2ecd5a1)

**Integrating Prometheus in to Grafana for Visualization** :

Monitoring FastAPI methods on Grafana,


![grafana](https://github.com/user-attachments/assets/d51f973d-217b-4c91-bca1-084cdb0c4276)












