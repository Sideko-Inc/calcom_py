import typing
import typing_extensions

from calcom_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from calcom_py.types import models, params


class MeClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.GetMeOutput:
        """
        Get my profile

        GET /v2/me

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.me.get()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/v2/me",
            auth_names=["bearerAuth"],
            cast_to=models.GetMeOutput,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        avatar_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_schedule_id: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        email_field: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        locale_field: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "ar",
                    "az",
                    "bg",
                    "ca",
                    "cs",
                    "da",
                    "de",
                    "el",
                    "en",
                    "es",
                    "es-419",
                    "et",
                    "eu",
                    "fi",
                    "fr",
                    "he",
                    "hr",
                    "hu",
                    "id",
                    "it",
                    "iw",
                    "ja",
                    "km",
                    "ko",
                    "lv",
                    "nl",
                    "no",
                    "pl",
                    "pt",
                    "pt-BR",
                    "ro",
                    "ru",
                    "sk",
                    "sr",
                    "sv",
                    "ta",
                    "th",
                    "tr",
                    "uk",
                    "vi",
                    "zh-CN",
                    "zh-TW",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        time_format: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        time_zone: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        week_start: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "Friday",
                    "Monday",
                    "Saturday",
                    "Sunday",
                    "Thursday",
                    "Tuesday",
                    "Wednesday",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.UpdateMeOutput:
        """
        Update my profile

        PATCH /v2/me

        Args:
            avatarUrl: URL of the user's avatar image
            defaultScheduleId: float
            email: str
            locale: typing_extensions.Literal["ar", "az", "bg", "ca", "cs", "da", "de", "el", "en", "es", "es-419", "et", "eu", "fi", "fr", "he", "hr", "hu", "id", "it", "iw", "ja", "km", "ko", "lv", "nl", "no", "pl", "pt", "pt-BR", "ro", "ru", "sk", "sr", "sv", "ta", "th", "tr", "uk", "vi", "zh-CN", "zh-TW"]
            name: str
            timeFormat: Must be 12 or 24
            timeZone: str
            weekStart: typing_extensions.Literal["Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"]
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.me.patch(
            avatar_url="https://cal.com/api/avatar/2b735186-b01b-46d3-87da-019b8f61776b.png",
            locale_field="en",
            time_format=12.0,
            week_start="Monday",
        )
        ```
        """
        _json = to_encodable(
            item={
                "avatar_url": avatar_url,
                "default_schedule_id": default_schedule_id,
                "email_field": email_field,
                "locale_field": locale_field,
                "name": name,
                "time_format": time_format,
                "time_zone": time_zone,
                "week_start": week_start,
            },
            dump_with=params._SerializerUpdateManagedUserInput,
        )
        return self._base_client.request(
            method="PATCH",
            path="/v2/me",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.UpdateMeOutput,
            request_options=request_options or default_request_options(),
        )


class AsyncMeClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.GetMeOutput:
        """
        Get my profile

        GET /v2/me

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.me.get()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/v2/me",
            auth_names=["bearerAuth"],
            cast_to=models.GetMeOutput,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        avatar_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_schedule_id: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        email_field: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        locale_field: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "ar",
                    "az",
                    "bg",
                    "ca",
                    "cs",
                    "da",
                    "de",
                    "el",
                    "en",
                    "es",
                    "es-419",
                    "et",
                    "eu",
                    "fi",
                    "fr",
                    "he",
                    "hr",
                    "hu",
                    "id",
                    "it",
                    "iw",
                    "ja",
                    "km",
                    "ko",
                    "lv",
                    "nl",
                    "no",
                    "pl",
                    "pt",
                    "pt-BR",
                    "ro",
                    "ru",
                    "sk",
                    "sr",
                    "sv",
                    "ta",
                    "th",
                    "tr",
                    "uk",
                    "vi",
                    "zh-CN",
                    "zh-TW",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        time_format: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        time_zone: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        week_start: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "Friday",
                    "Monday",
                    "Saturday",
                    "Sunday",
                    "Thursday",
                    "Tuesday",
                    "Wednesday",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.UpdateMeOutput:
        """
        Update my profile

        PATCH /v2/me

        Args:
            avatarUrl: URL of the user's avatar image
            defaultScheduleId: float
            email: str
            locale: typing_extensions.Literal["ar", "az", "bg", "ca", "cs", "da", "de", "el", "en", "es", "es-419", "et", "eu", "fi", "fr", "he", "hr", "hu", "id", "it", "iw", "ja", "km", "ko", "lv", "nl", "no", "pl", "pt", "pt-BR", "ro", "ru", "sk", "sr", "sv", "ta", "th", "tr", "uk", "vi", "zh-CN", "zh-TW"]
            name: str
            timeFormat: Must be 12 or 24
            timeZone: str
            weekStart: typing_extensions.Literal["Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"]
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.me.patch(
            avatar_url="https://cal.com/api/avatar/2b735186-b01b-46d3-87da-019b8f61776b.png",
            locale_field="en",
            time_format=12.0,
            week_start="Monday",
        )
        ```
        """
        _json = to_encodable(
            item={
                "avatar_url": avatar_url,
                "default_schedule_id": default_schedule_id,
                "email_field": email_field,
                "locale_field": locale_field,
                "name": name,
                "time_format": time_format,
                "time_zone": time_zone,
                "week_start": week_start,
            },
            dump_with=params._SerializerUpdateManagedUserInput,
        )
        return await self._base_client.request(
            method="PATCH",
            path="/v2/me",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.UpdateMeOutput,
            request_options=request_options or default_request_options(),
        )
