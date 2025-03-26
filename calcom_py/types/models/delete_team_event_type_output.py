import pydantic
import typing
import typing_extensions


class DeleteTeamEventTypeOutput(pydantic.BaseModel):
    """
    DeleteTeamEventTypeOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Dict[str, typing.Any] = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
