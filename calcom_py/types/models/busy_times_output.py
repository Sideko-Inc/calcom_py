import pydantic
import typing


class BusyTimesOutput(pydantic.BaseModel):
    """
    BusyTimesOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    end: str = pydantic.Field(
        alias="end",
    )
    source: typing.Optional[str] = pydantic.Field(alias="source", default=None)
    start: str = pydantic.Field(
        alias="start",
    )
