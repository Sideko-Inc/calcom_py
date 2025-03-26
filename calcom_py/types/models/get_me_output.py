import pydantic
import typing_extensions

from .me_output import MeOutput


class GetMeOutput(pydantic.BaseModel):
    """
    GetMeOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: MeOutput = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
