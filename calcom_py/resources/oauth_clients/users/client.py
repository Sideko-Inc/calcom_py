import typing
import typing_extensions

from calcom_py.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from calcom_py.resources.oauth_clients.users.force_refresh import (
    AsyncForceRefreshClient,
    ForceRefreshClient,
)
from calcom_py.types import models, params


class UsersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.force_refresh = ForceRefreshClient(base_client=self._base_client)

    def delete(
        self,
        *,
        client_id: str,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetManagedUserOutput:
        """
        Delete a managed user

        DELETE /v2/oauth-clients/{clientId}/users/{userId}

        Args:
            clientId: str
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth_clients.users.delete(client_id="string", user_id=123.0)
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/oauth-clients/{client_id}/users/{user_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetManagedUserOutput,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        client_id: str,
        emails: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        offset: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetManagedUsersOutput:
        """
        Get all managed users

        GET /v2/oauth-clients/{clientId}/users

        Args:
            emails: Filter managed users by email. If you want to filter by multiple emails, separate them with a comma.
            limit: The number of items to return
            offset: The number of items to skip
            clientId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth_clients.users.list(client_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(emails, type_utils.NotGiven):
            encode_query_param(
                _query,
                "emails",
                to_encodable(item=emails, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        if not isinstance(limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "limit",
                to_encodable(item=limit, dump_with=float),
                style="form",
                explode=True,
            )
        if not isinstance(offset, type_utils.NotGiven):
            encode_query_param(
                _query,
                "offset",
                to_encodable(item=offset, dump_with=float),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/v2/oauth-clients/{client_id}/users",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetManagedUsersOutput,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        client_id: str,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetManagedUserOutput:
        """
        Get a managed user

        GET /v2/oauth-clients/{clientId}/users/{userId}

        Args:
            clientId: str
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth_clients.users.get(client_id="string", user_id=123.0)
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/oauth-clients/{client_id}/users/{user_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetManagedUserOutput,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        client_id: str,
        user_id: float,
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
    ) -> models.GetManagedUserOutput:
        """
        Update a managed user

        PATCH /v2/oauth-clients/{clientId}/users/{userId}

        Args:
            avatarUrl: URL of the user's avatar image
            defaultScheduleId: float
            email: str
            locale: typing_extensions.Literal["ar", "az", "bg", "ca", "cs", "da", "de", "el", "en", "es", "es-419", "et", "eu", "fi", "fr", "he", "hr", "hu", "id", "it", "iw", "ja", "km", "ko", "lv", "nl", "no", "pl", "pt", "pt-BR", "ro", "ru", "sk", "sr", "sv", "ta", "th", "tr", "uk", "vi", "zh-CN", "zh-TW"]
            name: str
            timeFormat: Must be 12 or 24
            timeZone: str
            weekStart: typing_extensions.Literal["Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"]
            clientId: str
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth_clients.users.patch(
            client_id="string",
            user_id=123.0,
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
            path=f"/v2/oauth-clients/{client_id}/users/{user_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.GetManagedUserOutput,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        client_id: str,
        email_field: str,
        name: str,
        avatar_url: typing.Union[
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
    ) -> models.CreateManagedUserOutput:
        """
        Create a managed user

        POST /v2/oauth-clients/{clientId}/users

        Args:
            avatarUrl: URL of the user's avatar image
            locale: typing_extensions.Literal["ar", "az", "bg", "ca", "cs", "da", "de", "el", "en", "es", "es-419", "et", "eu", "fi", "fr", "he", "hr", "hu", "id", "it", "iw", "ja", "km", "ko", "lv", "nl", "no", "pl", "pt", "pt-BR", "ro", "ru", "sk", "sr", "sv", "ta", "th", "tr", "uk", "vi", "zh-CN", "zh-TW"]
            timeFormat: Must be a number 12 or 24
            timeZone: Timezone is used to create user's default schedule from Monday to Friday from 9AM to 5PM. If it is not passed then user does not have
              a default schedule and it must be created manually via the /schedules endpoint. Until the schedule is created, the user can't access availability atom to set his / her availability nor booked.
              It will default to Europe/London if not passed.
            weekStart: typing_extensions.Literal["Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"]
            clientId: str
            email: str
            name: Managed user's name is used in emails
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth_clients.users.create(
            client_id="string",
            email_field="alice@example.com",
            name="Alice Smith",
            avatar_url="https://cal.com/api/avatar/2b735186-b01b-46d3-87da-019b8f61776b.png",
            locale_field="en",
            time_format=12.0,
            time_zone="America/New_York",
            week_start="Monday",
        )
        ```
        """
        _json = to_encodable(
            item={
                "avatar_url": avatar_url,
                "locale_field": locale_field,
                "time_format": time_format,
                "time_zone": time_zone,
                "week_start": week_start,
                "email_field": email_field,
                "name": name,
            },
            dump_with=params._SerializerCreateManagedUserInput,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/oauth-clients/{client_id}/users",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreateManagedUserOutput,
            request_options=request_options or default_request_options(),
        )


class AsyncUsersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.force_refresh = AsyncForceRefreshClient(base_client=self._base_client)

    async def delete(
        self,
        *,
        client_id: str,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetManagedUserOutput:
        """
        Delete a managed user

        DELETE /v2/oauth-clients/{clientId}/users/{userId}

        Args:
            clientId: str
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth_clients.users.delete(client_id="string", user_id=123.0)
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/oauth-clients/{client_id}/users/{user_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetManagedUserOutput,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        client_id: str,
        emails: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        offset: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetManagedUsersOutput:
        """
        Get all managed users

        GET /v2/oauth-clients/{clientId}/users

        Args:
            emails: Filter managed users by email. If you want to filter by multiple emails, separate them with a comma.
            limit: The number of items to return
            offset: The number of items to skip
            clientId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth_clients.users.list(client_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(emails, type_utils.NotGiven):
            encode_query_param(
                _query,
                "emails",
                to_encodable(item=emails, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        if not isinstance(limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "limit",
                to_encodable(item=limit, dump_with=float),
                style="form",
                explode=True,
            )
        if not isinstance(offset, type_utils.NotGiven):
            encode_query_param(
                _query,
                "offset",
                to_encodable(item=offset, dump_with=float),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/v2/oauth-clients/{client_id}/users",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetManagedUsersOutput,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        client_id: str,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetManagedUserOutput:
        """
        Get a managed user

        GET /v2/oauth-clients/{clientId}/users/{userId}

        Args:
            clientId: str
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth_clients.users.get(client_id="string", user_id=123.0)
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/oauth-clients/{client_id}/users/{user_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetManagedUserOutput,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        client_id: str,
        user_id: float,
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
    ) -> models.GetManagedUserOutput:
        """
        Update a managed user

        PATCH /v2/oauth-clients/{clientId}/users/{userId}

        Args:
            avatarUrl: URL of the user's avatar image
            defaultScheduleId: float
            email: str
            locale: typing_extensions.Literal["ar", "az", "bg", "ca", "cs", "da", "de", "el", "en", "es", "es-419", "et", "eu", "fi", "fr", "he", "hr", "hu", "id", "it", "iw", "ja", "km", "ko", "lv", "nl", "no", "pl", "pt", "pt-BR", "ro", "ru", "sk", "sr", "sv", "ta", "th", "tr", "uk", "vi", "zh-CN", "zh-TW"]
            name: str
            timeFormat: Must be 12 or 24
            timeZone: str
            weekStart: typing_extensions.Literal["Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"]
            clientId: str
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth_clients.users.patch(
            client_id="string",
            user_id=123.0,
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
            path=f"/v2/oauth-clients/{client_id}/users/{user_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.GetManagedUserOutput,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        client_id: str,
        email_field: str,
        name: str,
        avatar_url: typing.Union[
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
    ) -> models.CreateManagedUserOutput:
        """
        Create a managed user

        POST /v2/oauth-clients/{clientId}/users

        Args:
            avatarUrl: URL of the user's avatar image
            locale: typing_extensions.Literal["ar", "az", "bg", "ca", "cs", "da", "de", "el", "en", "es", "es-419", "et", "eu", "fi", "fr", "he", "hr", "hu", "id", "it", "iw", "ja", "km", "ko", "lv", "nl", "no", "pl", "pt", "pt-BR", "ro", "ru", "sk", "sr", "sv", "ta", "th", "tr", "uk", "vi", "zh-CN", "zh-TW"]
            timeFormat: Must be a number 12 or 24
            timeZone: Timezone is used to create user's default schedule from Monday to Friday from 9AM to 5PM. If it is not passed then user does not have
              a default schedule and it must be created manually via the /schedules endpoint. Until the schedule is created, the user can't access availability atom to set his / her availability nor booked.
              It will default to Europe/London if not passed.
            weekStart: typing_extensions.Literal["Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"]
            clientId: str
            email: str
            name: Managed user's name is used in emails
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth_clients.users.create(
            client_id="string",
            email_field="alice@example.com",
            name="Alice Smith",
            avatar_url="https://cal.com/api/avatar/2b735186-b01b-46d3-87da-019b8f61776b.png",
            locale_field="en",
            time_format=12.0,
            time_zone="America/New_York",
            week_start="Monday",
        )
        ```
        """
        _json = to_encodable(
            item={
                "avatar_url": avatar_url,
                "locale_field": locale_field,
                "time_format": time_format,
                "time_zone": time_zone,
                "week_start": week_start,
                "email_field": email_field,
                "name": name,
            },
            dump_with=params._SerializerCreateManagedUserInput,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/oauth-clients/{client_id}/users",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreateManagedUserOutput,
            request_options=request_options or default_request_options(),
        )
