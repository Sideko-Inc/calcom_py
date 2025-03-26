import pydantic
import typing
import typing_extensions


class ScheduleAvailabilityInput20240611(typing_extensions.TypedDict):
    """
    ScheduleAvailabilityInput20240611
    """

    days: typing_extensions.Required[
        typing.List[
            typing_extensions.Literal[
                "Friday",
                "Monday",
                "Saturday",
                "Sunday",
                "Thursday",
                "Tuesday",
                "Wednesday",
            ]
        ]
    ]
    """
    Array of days when schedule is active.
    """

    end_time: typing_extensions.Required[str]
    """
    endTime must be a valid time in format HH:MM e.g. 15:00
    """

    start_time: typing_extensions.Required[str]
    """
    startTime must be a valid time in format HH:MM e.g. 08:00
    """


class _SerializerScheduleAvailabilityInput20240611(pydantic.BaseModel):
    """
    Serializer for ScheduleAvailabilityInput20240611 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    days: typing.List[
        typing_extensions.Literal[
            "Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"
        ]
    ] = pydantic.Field(
        alias="days",
    )
    end_time: str = pydantic.Field(
        alias="endTime",
    )
    start_time: str = pydantic.Field(
        alias="startTime",
    )
