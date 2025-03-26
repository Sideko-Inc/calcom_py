import pydantic
import typing_extensions

from .get_org_users_with_profile_output import GetOrgUsersWithProfileOutput


class GetOrganizationUserOutput(pydantic.BaseModel):
    """
    GetOrganizationUserOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: GetOrgUsersWithProfileOutput = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
