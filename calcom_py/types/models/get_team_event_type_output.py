import pydantic
import typing_extensions

from .team_event_type_output20240614 import TeamEventTypeOutput20240614


class GetTeamEventTypeOutput(pydantic.BaseModel):
    """
    GetTeamEventTypeOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: TeamEventTypeOutput20240614 = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
