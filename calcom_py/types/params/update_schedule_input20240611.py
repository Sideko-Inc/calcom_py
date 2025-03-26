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


class UpdateScheduleInput20240611(typing_extensions.TypedDict):
    """
    UpdateScheduleInput20240611
    """

    availability: typing_extensions.NotRequired[
        typing.List[ScheduleAvailabilityInput20240611]
    ]

    is_default: typing_extensions.NotRequired[bool]

    name: typing_extensions.NotRequired[str]

    overrides: typing_extensions.NotRequired[typing.List[ScheduleOverrideInput20240611]]

    time_zone: typing_extensions.NotRequired[str]


class _SerializerUpdateScheduleInput20240611(pydantic.BaseModel):
    """
    Serializer for UpdateScheduleInput20240611 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    availability: typing.Optional[
        typing.List[_SerializerScheduleAvailabilityInput20240611]
    ] = pydantic.Field(alias="availability", default=None)
    is_default: typing.Optional[bool] = pydantic.Field(alias="isDefault", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    overrides: typing.Optional[
        typing.List[_SerializerScheduleOverrideInput20240611]
    ] = pydantic.Field(alias="overrides", default=None)
    time_zone: typing.Optional[str] = pydantic.Field(alias="timeZone", default=None)
