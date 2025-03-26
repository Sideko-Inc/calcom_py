import pydantic
import typing


class LocationDefaultFieldOutput20240614(pydantic.BaseModel):
    """
    LocationDefaultFieldOutput20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    hidden: bool = pydantic.Field(
        alias="hidden",
    )
    """
    If true show under event type settings but don't show this booking field in the Booker. If false show in both.
    """
    is_default: typing.Dict[str, typing.Any] = pydantic.Field(
        alias="isDefault",
    )
    """
    This property is always true because it's a default field
    """
    required: bool = pydantic.Field(
        alias="required",
    )
    slug: str = pydantic.Field(
        alias="slug",
    )
    """
    This booking field is returned only if the event type has more than one location. The purpose of this field is to allow the user to select the location where the event will take place.
    """
    type_field: str = pydantic.Field(
        alias="type",
    )
