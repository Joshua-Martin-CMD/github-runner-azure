"""An Azure RM Python Pulumi program"""

from unicodedata import name
import pulumi

from pulumi_azure_native import (
    storage,
    resources,
    managedidentity as _identity
)

from resources.env_config import resource_grp, org, GITLAB_ORG, GITLAB_REPO

# Create an Azure Resource Group
resource_group = resources.ResourceGroup(f"{resource_grp}")

# Create an Azure resource (Federated Access)
federated_github_access = _identity.FederatedIdentityCredential(f"Gitlab-OIDC",
    name=f"Gitlab_runner-{org}",
    issuer="https://token.actions.githubusercontent.com",
    subject=f"repo:{GITLAB_ORG}/{GITLAB_REPO}:environment:Master",
    resource_name=f"{resource_grp}",
    audiences=["api://AzureADTokenExchange"]
    )
