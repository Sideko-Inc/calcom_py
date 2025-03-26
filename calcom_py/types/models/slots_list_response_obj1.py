import pydantic
import typing

from .slots_list_response_obj1_additional_props_item import (
    SlotsListResponseObj1AdditionalPropsItem,
)


class SlotsListResponseObj1(pydantic.BaseModel):
    """
    SlotsListResponseObj1
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[
        str, typing.List[SlotsListResponseObj1AdditionalPropsItem]
    ]
