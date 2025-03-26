import pydantic
import typing
import typing_extensions

from .schedule_availability_input20240611 import (
    ScheduleAvailabilityInput20240611,
    _SerializerScheduleAvailabilityInput20240611,
)
from .schedule_override_input20240611 import (
    ScheduleOverrideInput20240611,
    _SerializerScheduleOverrideInput20240611,
)


class CreateScheduleInput20240611(typing_extensions.TypedDict):
    """
    CreateScheduleInput20240611
    """

    availability: typing_extensions.NotRequired[
        typing.List[ScheduleAvailabilityInput20240611]
    ]
    """
    Each object contains days and times when the user is available. If not passed, the default availability is Monday to Friday from 09:00 to 17:00.
    """

    is_default: typing_extensions.Required[bool]
    """
    Each user should have 1 default schedule. If you specified `timeZone` when creating managed user, then the default schedule will be created with that timezone.
        Default schedule means that if an event type is not tied to a specific schedule then the default schedule is used.
    """

    name: typing_extensions.Required[str]

    overrides: typing_extensions.NotRequired[typing.List[ScheduleOverrideInput20240611]]
    """
    Need to change availability for a specific date? Add an override.
    """

    time_zone: typing_extensions.Required[str]
    """
    Timezone is used to calculate available times when an event using the schedule is booked.
    """


class _SerializerCreateScheduleInput20240611(pydantic.BaseModel):
    """
    Serializer for CreateScheduleInput20240611 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    availability: typing.Optional[
        typing.List[_SerializerScheduleAvailabilityInput20240611]
    ] = pydantic.Field(alias="availability", default=None)
    is_default: bool = pydantic.Field(
        alias="isDefault",
    )
    name: str = pydantic.Field(
        alias="name",
    )
    overrides: typing.Optional[
        typing.List[_SerializerScheduleOverrideInput20240611]
    ] = pydantic.Field(alias="overrides", default=None)
    time_zone: str = pydantic.Field(
        alias="timeZone",
    )
