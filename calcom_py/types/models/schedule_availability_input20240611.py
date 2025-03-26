import pydantic
import typing
import typing_extensions


class ScheduleAvailabilityInput20240611(pydantic.BaseModel):
    """
    ScheduleAvailabilityInput20240611
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    days: typing.List[
        typing_extensions.Literal[
            "Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"
        ]
    ] = pydantic.Field(
        alias="days",
    )
    """
    Array of days when schedule is active.
    """
    end_time: str = pydantic.Field(
        alias="endTime",
    )
    """
    endTime must be a valid time in format HH:MM e.g. 15:00
    """
    start_time: str = pydantic.Field(
        alias="startTime",
    )
    """
    startTime must be a valid time in format HH:MM e.g. 08:00
    """
