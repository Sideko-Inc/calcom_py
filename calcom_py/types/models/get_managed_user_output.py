import pydantic
import typing_extensions

from .managed_user_output import ManagedUserOutput


class GetManagedUserOutput(pydantic.BaseModel):
    """
    GetManagedUserOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: ManagedUserOutput = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
