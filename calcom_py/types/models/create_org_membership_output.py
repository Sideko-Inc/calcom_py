import pydantic
import typing_extensions

from .org_membership_output_dto import OrgMembershipOutputDto


class CreateOrgMembershipOutput(pydantic.BaseModel):
    """
    CreateOrgMembershipOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: OrgMembershipOutputDto = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
