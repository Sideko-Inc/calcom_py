import pydantic
import typing_extensions

from .attribute import Attribute


class GetSingleAttributeOutput(pydantic.BaseModel):
    """
    GetSingleAttributeOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: Attribute = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
