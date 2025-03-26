import pydantic
import typing
import typing_extensions

from .team_event_type_output20240614 import TeamEventTypeOutput20240614


class GetTeamEventTypesOutput(pydantic.BaseModel):
    """
    GetTeamEventTypesOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[TeamEventTypeOutput20240614] = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
