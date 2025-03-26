import pydantic
import typing


class CreateIcsFeedOutput(pydantic.BaseModel):
    """
    CreateIcsFeedOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app_id: typing.Optional[str] = pydantic.Field(
        alias="appId",
    )
    """
    The slug of the calendar
    """
    id: float = pydantic.Field(
        alias="id",
    )
    """
    The id of the calendar credential
    """
    invalid: typing.Optional[bool] = pydantic.Field(
        alias="invalid",
    )
    """
    Whether the calendar credentials are valid or not
    """
    team_id: typing.Optional[int] = pydantic.Field(
        alias="teamId",
    )
    """
    The team id of the user that created the calendar
    """
    type_field: str = pydantic.Field(
        alias="type",
    )
    """
    The type of the calendar
    """
    user_id: typing.Optional[int] = pydantic.Field(
        alias="userId",
    )
    """
    The user id of the user that created the calendar
    """
