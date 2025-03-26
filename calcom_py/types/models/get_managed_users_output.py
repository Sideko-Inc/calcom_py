import pydantic
import typing
import typing_extensions

from .managed_user_output import ManagedUserOutput


class GetManagedUsersOutput(pydantic.BaseModel):
    """
    GetManagedUsersOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[ManagedUserOutput] = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
