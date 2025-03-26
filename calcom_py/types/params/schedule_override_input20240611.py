import pydantic
import typing_extensions


class ScheduleOverrideInput20240611(typing_extensions.TypedDict):
    """
    ScheduleOverrideInput20240611
    """

    date: typing_extensions.Required[str]

    end_time: typing_extensions.Required[str]
    """
    endTime must be a valid time in format HH:MM e.g. 13:00
    """

    start_time: typing_extensions.Required[str]
    """
    startTime must be a valid time in format HH:MM e.g. 12:00
    """


class _SerializerScheduleOverrideInput20240611(pydantic.BaseModel):
    """
    Serializer for ScheduleOverrideInput20240611 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    date: str = pydantic.Field(
        alias="date",
    )
    end_time: str = pydantic.Field(
        alias="endTime",
    )
    start_time: str = pydantic.Field(
        alias="startTime",
    )
