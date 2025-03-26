import pydantic
import typing
import typing_extensions


class BookerLayouts20240614(typing_extensions.TypedDict):
    """
    BookerLayouts20240614
    """

    default_layout: typing_extensions.Required[
        typing_extensions.Literal["column", "month", "week"]
    ]

    enabled_layouts: typing_extensions.Required[
        typing.List[typing_extensions.Literal["column", "month", "week"]]
    ]


class _SerializerBookerLayouts20240614(pydantic.BaseModel):
    """
    Serializer for BookerLayouts20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
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
