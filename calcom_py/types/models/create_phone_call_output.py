import pydantic
import typing_extensions

from .data import Data


class CreatePhoneCallOutput(pydantic.BaseModel):
    """
    CreatePhoneCallOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: Data = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
