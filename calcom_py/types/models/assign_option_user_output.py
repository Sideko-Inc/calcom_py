import pydantic
import typing_extensions

from .assign_option_user_output_data import AssignOptionUserOutputData


class AssignOptionUserOutput(pydantic.BaseModel):
    """
    AssignOptionUserOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: AssignOptionUserOutputData = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
