import pydantic
import typing


class DeletedCalendarCredentialsOutputDto(pydantic.BaseModel):
    """
    DeletedCalendarCredentialsOutputDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app_id: typing.Optional[str] = pydantic.Field(
        alias="appId",
    )
    id: float = pydantic.Field(
        alias="id",
    )
    invalid: typing.Optional[bool] = pydantic.Field(
        alias="invalid",
    )
    team_id: typing.Optional[float] = pydantic.Field(
        alias="teamId",
    )
    type_field: str = pydantic.Field(
        alias="type",
    )
    user_id: typing.Optional[float] = pydantic.Field(
        alias="userId",
    )
