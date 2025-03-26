import pydantic
import typing_extensions

from .managed_organization_with_api_key_output import (
    ManagedOrganizationWithApiKeyOutput,
)


class CreateManagedOrganizationOutput(pydantic.BaseModel):
    """
    CreateManagedOrganizationOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: ManagedOrganizationWithApiKeyOutput = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
