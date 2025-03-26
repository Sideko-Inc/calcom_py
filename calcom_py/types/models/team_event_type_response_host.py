import pydantic
import typing
import typing_extensions


class TeamEventTypeResponseHost(pydantic.BaseModel):
    """
    TeamEventTypeResponseHost
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    avatar_url: typing.Optional[str] = pydantic.Field(alias="avatarUrl", default=None)
    mandatory: typing.Optional[bool] = pydantic.Field(alias="mandatory", default=None)
    """
    Only relevant for round robin event types. If true then the user must attend round robin event always.
    """
    name: str = pydantic.Field(
        alias="name",
    )
    priority: typing.Optional[
        typing_extensions.Literal["high", "highest", "low", "lowest", "medium"]
    ] = pydantic.Field(alias="priority", default=None)
    user_id: float = pydantic.Field(
        alias="userId",
    )
    """
    Which user is the host of this event
    """
