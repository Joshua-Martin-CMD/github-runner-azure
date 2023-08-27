# Docker Runner for Github in Azure

![IaC - Provider](https://img.shields.io/badge/IaC_Provider-Pulumi-8A2BE2?logo=pulumi) ![Cloud provider](https://img.shields.io/badge/Cloud-Azure-blue?logo=microsoftazure) ![Lang - Python](https://img.shields.io/badge/Language-Python-blue?logo=python)

Deployed with Pulumi we are creating the following resources
- ACR (Azure Container Registry) 
- ACA (Azure Container App)
- Resource Group

to deploy each resource in the correct order, deploy the ACR repo first so we can then push the github images into the ACR Repo to reuse in ACA. 

![Diagram](diagrams/Azure_Deploy.jpg)