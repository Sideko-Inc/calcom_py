import pydantic
import typing
import typing_extensions

from .busy_times_output import BusyTimesOutput


class GetBusyTimesOutput(pydantic.BaseModel):
    """
    GetBusyTimesOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[BusyTimesOutput] = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
