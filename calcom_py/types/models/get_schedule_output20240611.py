import pydantic
import typing
import typing_extensions

from .schedule_output20240611 import ScheduleOutput20240611


class GetScheduleOutput20240611(pydantic.BaseModel):
    """
    GetScheduleOutput20240611
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: ScheduleOutput20240611 = pydantic.Field(
        alias="data",
    )
    error: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="error", default=None
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
