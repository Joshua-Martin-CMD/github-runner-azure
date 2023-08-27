"""An Azure RM Python Pulumi program"""

import pulumi
from pulumi_azure_native import storage
from pulumi_azure_native import resources
import pulumi_azure_native as azure_native

from resources.env_config import PROJ_NAME

# Create an Azure Resource Group
resource_group = resources.ResourceGroup(f"{PROJ_NAME}-resource-group")

# Create an Azure Registry
registry = azure_native.containerregistry.Registry(
    f"{PROJ_NAME}Registry",
    admin_user_enabled=True,
    location="australiaeast",
    registry_name="githubrunnerregistry",
    resource_group_name=resource_group.name,
    sku=azure_native.containerregistry.SkuArgs(
        name="Standard",
    ),
    tags={
        "Project": f"{PROJ_NAME}",
    }
)
# Create an Azure resource (Storage Account)
account = storage.StorageAccount(
    "sa",
    resource_group_name=resource_group.name,
    sku=storage.SkuArgs(
        name=storage.SkuName.STANDARD_LRS,
    ),
    kind=storage.Kind.STORAGE_V2,
)

# Export the primary key of the Storage Account
primary_key = (
    pulumi.Output.all(resource_group.name, account.name)
    .apply(
        lambda args: storage.list_storage_account_keys(
            resource_group_name=args[0], account_name=args[1]
        )
    )
    .apply(lambda accountKeys: accountKeys.keys[0].value)
)

pulumi.export("primary_storage_key", primary_key)
