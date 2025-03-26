import pydantic
import typing_extensions

from .managed_organization_output import ManagedOrganizationOutput


class GetManagedOrganizationOutput(pydantic.BaseModel):
    """
    GetManagedOrganizationOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: ManagedOrganizationOutput = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
