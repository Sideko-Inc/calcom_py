import pydantic
import typing
import typing_extensions

from .create_managed_user_data import CreateManagedUserData


class CreateManagedUserOutput(pydantic.BaseModel):
    """
    CreateManagedUserOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: CreateManagedUserData = pydantic.Field(
        alias="data",
    )
    error: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="error", default=None
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
