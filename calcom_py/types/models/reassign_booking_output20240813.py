import pydantic
import typing
import typing_extensions


class ReassignBookingOutput20240813(pydantic.BaseModel):
    """
    ReassignBookingOutput20240813
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Dict[str, typing.Any] = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
