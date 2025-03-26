import pydantic
import typing


class ProfileOutput(pydantic.BaseModel):
    """
    ProfileOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: float = pydantic.Field(
        alias="id",
    )
    """
    The ID of the profile of user
    """
    organization_id: float = pydantic.Field(
        alias="organizationId",
    )
    """
    The ID of the organization of user
    """
    user_id: float = pydantic.Field(
        alias="userId",
    )
    """
    The IDof the user
    """
    username: typing.Optional[str] = pydantic.Field(alias="username", default=None)
    """
    The username of the user within the organization context
    """
