import pydantic
import typing
import typing_extensions

from .managed_organization_output import ManagedOrganizationOutput


class GetManagedOrganizationsOutput(pydantic.BaseModel):
    """
    GetManagedOrganizationsOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[ManagedOrganizationOutput] = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
