import pydantic
import typing_extensions


class DeleteScheduleOutput20240611(pydantic.BaseModel):
    """
    DeleteScheduleOutput20240611
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
