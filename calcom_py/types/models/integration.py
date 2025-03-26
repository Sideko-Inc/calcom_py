import pydantic
import typing


class Integration(pydantic.BaseModel):
    """
    Integration
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    field_template: typing.Optional[str] = pydantic.Field(
        alias="__template", default=None
    )
    app_data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="appData", default=None
    )
    categories: typing.List[str] = pydantic.Field(
        alias="categories",
    )
    category: typing.Optional[str] = pydantic.Field(alias="category", default=None)
    description: str = pydantic.Field(
        alias="description",
    )
    dir_name: typing.Optional[str] = pydantic.Field(alias="dirName", default=None)
    email_field: str = pydantic.Field(
        alias="email",
    )
    installed: typing.Optional[bool] = pydantic.Field(alias="installed", default=None)
    location_option: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="locationOption",
    )
    logo: str = pydantic.Field(
        alias="logo",
    )
    name: str = pydantic.Field(
        alias="name",
    )
    publisher: str = pydantic.Field(
        alias="publisher",
    )
    slug: str = pydantic.Field(
        alias="slug",
    )
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
    type_field: str = pydantic.Field(
        alias="type",
    )
    url: str = pydantic.Field(
        alias="url",
    )
    variant: str = pydantic.Field(
        alias="variant",
    )
