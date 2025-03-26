import pydantic


class BookingHost(pydantic.BaseModel):
    """
    BookingHost
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    email_field: str = pydantic.Field(
        alias="email",
    )
    id: float = pydantic.Field(
        alias="id",
    )
    name: str = pydantic.Field(
        alias="name",
    )
    time_zone: str = pydantic.Field(
        alias="timeZone",
    )
    username: str = pydantic.Field(
        alias="username",
    )
