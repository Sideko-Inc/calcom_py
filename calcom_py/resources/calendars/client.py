import httpx
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
from calcom_py.resources.calendars.credentials import (
    AsyncCredentialsClient,
    CredentialsClient,
)
from calcom_py.resources.calendars.ics_feed import AsyncIcsFeedClient, IcsFeedClient
from calcom_py.types import models, params


class CalendarsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.ics_feed = IcsFeedClient(base_client=self._base_client)
        self.credentials = CredentialsClient(base_client=self._base_client)

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ConnectedCalendarsOutput:
        """
        Get all calendars

        GET /v2/calendars

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.calendars.list()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/v2/calendars",
            auth_names=["bearerAuth"],
            cast_to=models.ConnectedCalendarsOutput,
            request_options=request_options or default_request_options(),
        )

    def get_busy(
        self,
        *,
        credential_id: float,
        external_id: str,
        logged_in_users_tz: str,
        date_from: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        date_to: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetBusyTimesOutput:
        """
        Get busy times

        Get busy times from a calendar. Example request URL is `https://api.cal.com/v2/calendars/busy-times?loggedInUsersTz=Europe%2FMadrid&dateFrom=2024-12-18&dateTo=2024-12-18&calendarsToLoad[0][credentialId]=135&calendarsToLoad[0][externalId]=skrauciz%40gmail.com`

        GET /v2/calendars/busy-times

        Args:
            dateFrom: The starting date for the busy times query
            dateTo: The ending date for the busy times query
            credentialId: float
            externalId: str
            loggedInUsersTz: The timezone of the logged in user represented as a string
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.calendars.get_busy(
            credential_id=123.0, external_id="string", logged_in_users_tz="string"
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "credentialId",
            to_encodable(item=credential_id, dump_with=float),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "externalId",
            to_encodable(item=external_id, dump_with=str),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "loggedInUsersTz",
            to_encodable(item=logged_in_users_tz, dump_with=str),
            style="form",
            explode=True,
        )
        if not isinstance(date_from, type_utils.NotGiven):
            encode_query_param(
                _query,
                "dateFrom",
                to_encodable(item=date_from, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(date_to, type_utils.NotGiven):
            encode_query_param(
                _query,
                "dateTo",
                to_encodable(item=date_to, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v2/calendars/busy-times",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetBusyTimesOutput,
            request_options=request_options or default_request_options(),
        )

    def check(
        self,
        *,
        calendar_field: typing_extensions.Literal["apple", "google", "office365"],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Check a calendar connection

        GET /v2/calendars/{calendar}/check

        Args:
            calendar: typing_extensions.Literal["apple", "google", "office365"]
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.calendars.check(calendar_field="apple")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/calendars/{calendar_field}/check",
            auth_names=["bearerAuth"],
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )

    def connect(
        self,
        *,
        calendar_field: typing_extensions.Literal["google", "office365"],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Get oAuth connect URL

        GET /v2/calendars/{calendar}/connect

        Args:
            calendar: typing_extensions.Literal["google", "office365"]
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.calendars.connect(calendar_field="google")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/calendars/{calendar_field}/connect",
            auth_names=["bearerAuth"],
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )

    def save(
        self,
        *,
        calendar_field: typing_extensions.Literal["google", "office365"],
        code_field: str,
        state: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Save an oAuth calendar credentials

        GET /v2/calendars/{calendar}/save

        Args:
            calendar: typing_extensions.Literal["google", "office365"]
            code: str
            state: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.calendars.save(
            calendar_field="google", code_field="string", state="string"
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "code",
            to_encodable(item=code_field, dump_with=str),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "state",
            to_encodable(item=state, dump_with=str),
            style="form",
            explode=True,
        )
        return self._base_client.request(
            method="GET",
            path=f"/v2/calendars/{calendar_field}/save",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    def disconnect(
        self,
        *,
        calendar_field: typing_extensions.Literal["apple", "google", "office365"],
        id: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeletedCalendarCredentialsOutputResponseDto:
        """
        Disconnect a calendar

        POST /v2/calendars/{calendar}/disconnect

        Args:
            calendar: typing_extensions.Literal["apple", "google", "office365"]
            id: Credential ID of the calendar to delete, as returned by the /calendars endpoint
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.calendars.disconnect(calendar_field="apple", id=10)
        ```
        """
        _json = to_encodable(
            item={"id": id},
            dump_with=params._SerializerDeleteCalendarCredentialsInputBodyDto,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/calendars/{calendar_field}/disconnect",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.DeletedCalendarCredentialsOutputResponseDto,
            request_options=request_options or default_request_options(),
        )


class AsyncCalendarsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.ics_feed = AsyncIcsFeedClient(base_client=self._base_client)
        self.credentials = AsyncCredentialsClient(base_client=self._base_client)

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ConnectedCalendarsOutput:
        """
        Get all calendars

        GET /v2/calendars

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.calendars.list()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/v2/calendars",
            auth_names=["bearerAuth"],
            cast_to=models.ConnectedCalendarsOutput,
            request_options=request_options or default_request_options(),
        )

    async def get_busy(
        self,
        *,
        credential_id: float,
        external_id: str,
        logged_in_users_tz: str,
        date_from: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        date_to: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetBusyTimesOutput:
        """
        Get busy times

        Get busy times from a calendar. Example request URL is `https://api.cal.com/v2/calendars/busy-times?loggedInUsersTz=Europe%2FMadrid&dateFrom=2024-12-18&dateTo=2024-12-18&calendarsToLoad[0][credentialId]=135&calendarsToLoad[0][externalId]=skrauciz%40gmail.com`

        GET /v2/calendars/busy-times

        Args:
            dateFrom: The starting date for the busy times query
            dateTo: The ending date for the busy times query
            credentialId: float
            externalId: str
            loggedInUsersTz: The timezone of the logged in user represented as a string
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.calendars.get_busy(
            credential_id=123.0, external_id="string", logged_in_users_tz="string"
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "credentialId",
            to_encodable(item=credential_id, dump_with=float),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "externalId",
            to_encodable(item=external_id, dump_with=str),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "loggedInUsersTz",
            to_encodable(item=logged_in_users_tz, dump_with=str),
            style="form",
            explode=True,
        )
        if not isinstance(date_from, type_utils.NotGiven):
            encode_query_param(
                _query,
                "dateFrom",
                to_encodable(item=date_from, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(date_to, type_utils.NotGiven):
            encode_query_param(
                _query,
                "dateTo",
                to_encodable(item=date_to, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v2/calendars/busy-times",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetBusyTimesOutput,
            request_options=request_options or default_request_options(),
        )

    async def check(
        self,
        *,
        calendar_field: typing_extensions.Literal["apple", "google", "office365"],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Check a calendar connection

        GET /v2/calendars/{calendar}/check

        Args:
            calendar: typing_extensions.Literal["apple", "google", "office365"]
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.calendars.check(calendar_field="apple")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/calendars/{calendar_field}/check",
            auth_names=["bearerAuth"],
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )

    async def connect(
        self,
        *,
        calendar_field: typing_extensions.Literal["google", "office365"],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Get oAuth connect URL

        GET /v2/calendars/{calendar}/connect

        Args:
            calendar: typing_extensions.Literal["google", "office365"]
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.calendars.connect(calendar_field="google")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/calendars/{calendar_field}/connect",
            auth_names=["bearerAuth"],
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )

    async def save(
        self,
        *,
        calendar_field: typing_extensions.Literal["google", "office365"],
        code_field: str,
        state: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Save an oAuth calendar credentials

        GET /v2/calendars/{calendar}/save

        Args:
            calendar: typing_extensions.Literal["google", "office365"]
            code: str
            state: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.calendars.save(
            calendar_field="google", code_field="string", state="string"
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "code",
            to_encodable(item=code_field, dump_with=str),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "state",
            to_encodable(item=state, dump_with=str),
            style="form",
            explode=True,
        )
        return await self._base_client.request(
            method="GET",
            path=f"/v2/calendars/{calendar_field}/save",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    async def disconnect(
        self,
        *,
        calendar_field: typing_extensions.Literal["apple", "google", "office365"],
        id: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeletedCalendarCredentialsOutputResponseDto:
        """
        Disconnect a calendar

        POST /v2/calendars/{calendar}/disconnect

        Args:
            calendar: typing_extensions.Literal["apple", "google", "office365"]
            id: Credential ID of the calendar to delete, as returned by the /calendars endpoint
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.calendars.disconnect(calendar_field="apple", id=10)
        ```
        """
        _json = to_encodable(
            item={"id": id},
            dump_with=params._SerializerDeleteCalendarCredentialsInputBodyDto,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/calendars/{calendar_field}/disconnect",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.DeletedCalendarCredentialsOutputResponseDto,
            request_options=request_options or default_request_options(),
        )
