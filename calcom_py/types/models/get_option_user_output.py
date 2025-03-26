import pydantic
import typing
import typing_extensions

from .get_option_user_output_data1 import GetOptionUserOutputData1


class GetOptionUserOutput(pydantic.BaseModel):
    """
    GetOptionUserOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[GetOptionUserOutputData1] = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
