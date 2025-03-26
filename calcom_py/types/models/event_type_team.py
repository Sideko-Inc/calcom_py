import pydantic
import typing


class EventTypeTeam(pydantic.BaseModel):
    """
    EventTypeTeam
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    banner_url: typing.Optional[str] = pydantic.Field(alias="bannerUrl", default=None)
    brand_color: typing.Optional[str] = pydantic.Field(alias="brandColor", default=None)
    dark_brand_color: typing.Optional[str] = pydantic.Field(
        alias="darkBrandColor", default=None
    )
    id: float = pydantic.Field(
        alias="id",
    )
    logo_url: typing.Optional[str] = pydantic.Field(alias="logoUrl", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    slug: typing.Optional[str] = pydantic.Field(alias="slug", default=None)
    theme: typing.Optional[str] = pydantic.Field(alias="theme", default=None)
    week_start: typing.Optional[str] = pydantic.Field(alias="weekStart", default=None)
