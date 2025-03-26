import pydantic
import typing

from .schedule_availability_input20240611 import ScheduleAvailabilityInput20240611
from .schedule_override_input20240611 import ScheduleOverrideInput20240611


class ScheduleOutput20240611(pydantic.BaseModel):
    """
    ScheduleOutput20240611
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    availability: typing.List[ScheduleAvailabilityInput20240611] = pydantic.Field(
        alias="availability",
    )
    id: float = pydantic.Field(
        alias="id",
    )
    is_default: bool = pydantic.Field(
        alias="isDefault",
    )
    name: str = pydantic.Field(
        alias="name",
    )
    overrides: typing.List[ScheduleOverrideInput20240611] = pydantic.Field(
        alias="overrides",
    )
    owner_id: float = pydantic.Field(
        alias="ownerId",
    )
    time_zone: str = pydantic.Field(
        alias="timeZone",
    )
