import pydantic
import typing


class SlotsListResponseObj0(pydantic.BaseModel):
    """
    SlotsListResponseObj0
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.List[str]]
