import pydantic
import typing
import typing_extensions

from .option_output import OptionOutput


class GetAllAttributeOptionOutput(pydantic.BaseModel):
    """
    GetAllAttributeOptionOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[OptionOutput] = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
