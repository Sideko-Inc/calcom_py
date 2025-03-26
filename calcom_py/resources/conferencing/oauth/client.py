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
)
from calcom_py.types import models


class OauthClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def auth_url(
        self,
        *,
        app: typing_extensions.Literal["msteams", "zoom"],
        on_error_return_to: str,
        return_to: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetConferencingAppsOauthUrlResponseDto:
        """
        Get OAuth conferencing app auth url

        GET /v2/conferencing/{app}/oauth/auth-url

        Args:
            app: Conferencing application type
            onErrorReturnTo: str
            returnTo: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.conferencing.oauth.auth_url(
            app="msteams", on_error_return_to="string", return_to="string"
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "onErrorReturnTo",
            to_encodable(item=on_error_return_to, dump_with=str),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "returnTo",
            to_encodable(item=return_to, dump_with=str),
            style="form",
            explode=True,
        )
        return self._base_client.request(
            method="GET",
            path=f"/v2/conferencing/{app}/oauth/auth-url",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetConferencingAppsOauthUrlResponseDto,
            request_options=request_options or default_request_options(),
        )

    def callback(
        self,
        *,
        app: typing_extensions.Literal["msteams", "zoom"],
        code_field: str,
        state: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        conferencing apps oauths callback

        GET /v2/conferencing/{app}/oauth/callback

        Args:
            app: Conferencing application type
            code: str
            state: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.conferencing.oauth.callback(
            app="msteams", code_field="string", state="string"
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
            path=f"/v2/conferencing/{app}/oauth/callback",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )


class AsyncOauthClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def auth_url(
        self,
        *,
        app: typing_extensions.Literal["msteams", "zoom"],
        on_error_return_to: str,
        return_to: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetConferencingAppsOauthUrlResponseDto:
        """
        Get OAuth conferencing app auth url

        GET /v2/conferencing/{app}/oauth/auth-url

        Args:
            app: Conferencing application type
            onErrorReturnTo: str
            returnTo: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.conferencing.oauth.auth_url(
            app="msteams", on_error_return_to="string", return_to="string"
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "onErrorReturnTo",
            to_encodable(item=on_error_return_to, dump_with=str),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "returnTo",
            to_encodable(item=return_to, dump_with=str),
            style="form",
            explode=True,
        )
        return await self._base_client.request(
            method="GET",
            path=f"/v2/conferencing/{app}/oauth/auth-url",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetConferencingAppsOauthUrlResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def callback(
        self,
        *,
        app: typing_extensions.Literal["msteams", "zoom"],
        code_field: str,
        state: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        conferencing apps oauths callback

        GET /v2/conferencing/{app}/oauth/callback

        Args:
            app: Conferencing application type
            code: str
            state: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.conferencing.oauth.callback(
            app="msteams", code_field="string", state="string"
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
            path=f"/v2/conferencing/{app}/oauth/callback",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )
