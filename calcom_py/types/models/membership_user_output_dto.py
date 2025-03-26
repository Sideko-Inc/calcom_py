import pydantic
import typing


class MembershipUserOutputDto(pydantic.BaseModel):
    """
    MembershipUserOutputDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    avatar_url: typing.Optional[str] = pydantic.Field(alias="avatarUrl", default=None)
    email_field: str = pydantic.Field(
        alias="email",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    username: typing.Optional[str] = pydantic.Field(alias="username", default=None)
