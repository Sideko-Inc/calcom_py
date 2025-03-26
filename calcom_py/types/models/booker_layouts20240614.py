import pydantic
import typing
import typing_extensions


class BookerLayouts20240614(pydantic.BaseModel):
    """
    BookerLayouts20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    default_layout: typing_extensions.Literal["column", "month", "week"] = (
        pydantic.Field(
            alias="defaultLayout",
        )
    )
    enabled_layouts: typing.List[
        typing_extensions.Literal["column", "month", "week"]
    ] = pydantic.Field(
        alias="enabledLayouts",
    )
