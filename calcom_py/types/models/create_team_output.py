import pydantic
import typing
import typing_extensions


class CreateTeamOutput(pydantic.BaseModel):
    """
    CreateTeamOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Dict[str, typing.Any] = pydantic.Field(
        alias="data",
    )
    """
    Either an Output object or a TeamOutputDto.
    """
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
