import pydantic


class ScheduleOverrideInput20240611(pydantic.BaseModel):
    """
    ScheduleOverrideInput20240611
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    date: str = pydantic.Field(
        alias="date",
    )
    end_time: str = pydantic.Field(
        alias="endTime",
    )
    """
    endTime must be a valid time in format HH:MM e.g. 13:00
    """
    start_time: str = pydantic.Field(
        alias="startTime",
    )
    """
    startTime must be a valid time in format HH:MM e.g. 12:00
    """
