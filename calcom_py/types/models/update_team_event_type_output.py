import pydantic
import typing
import typing_extensions

from .team_event_type_output20240614 import TeamEventTypeOutput20240614


class UpdateTeamEventTypeOutput(pydantic.BaseModel):
    """
    UpdateTeamEventTypeOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Union[
        TeamEventTypeOutput20240614, typing.List[TeamEventTypeOutput20240614]
    ] = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
