import typing
import typing_extensions

from calcom_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from calcom_py.resources.conferencing.oauth import AsyncOauthClient, OauthClient
from calcom_py.types import models


class ConferencingClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.oauth = OauthClient(base_client=self._base_client)

    def disconnect(
        self,
        *,
        app: typing_extensions.Literal["google-meet", "msteams", "zoom"],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DisconnectConferencingAppOutputResponseDto:
        """
        Disconnect your conferencing application

        DELETE /v2/conferencing/{app}/disconnect

        Args:
            app: Conferencing application type
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.conferencing.disconnect(app="google-meet")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/conferencing/{app}/disconnect",
            auth_names=["bearerAuth"],
            cast_to=models.DisconnectConferencingAppOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ConferencingAppsOutputResponseDto:
        """
        List your conferencing applications

        GET /v2/conferencing

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.conferencing.list()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/v2/conferencing",
            auth_names=["bearerAuth"],
            cast_to=models.ConferencingAppsOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def list_1(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.GetDefaultConferencingAppOutputResponseDto:
        """
        Get your default conferencing application

        GET /v2/conferencing/default

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.conferencing.list_1()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/v2/conferencing/default",
            auth_names=["bearerAuth"],
            cast_to=models.GetDefaultConferencingAppOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def connect(
        self,
        *,
        app: typing_extensions.Literal["google-meet"],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ConferencingAppOutputResponseDto:
        """
        Connect your conferencing application

        POST /v2/conferencing/{app}/connect

        Args:
            app: Conferencing application type
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.conferencing.connect(app="google-meet")
        ```
        """
        return self._base_client.request(
            method="POST",
            path=f"/v2/conferencing/{app}/connect",
            auth_names=["bearerAuth"],
            cast_to=models.ConferencingAppOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def default(
        self,
        *,
        app: typing_extensions.Literal["daily-video", "google-meet", "msteams", "zoom"],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SetDefaultConferencingAppOutputResponseDto:
        """
        Set your default conferencing application

        POST /v2/conferencing/{app}/default

        Args:
            app: Conferencing application type
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.conferencing.default(app="daily-video")
        ```
        """
        return self._base_client.request(
            method="POST",
            path=f"/v2/conferencing/{app}/default",
            auth_names=["bearerAuth"],
            cast_to=models.SetDefaultConferencingAppOutputResponseDto,
            request_options=request_options or default_request_options(),
        )


class AsyncConferencingClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.oauth = AsyncOauthClient(base_client=self._base_client)

    async def disconnect(
        self,
        *,
        app: typing_extensions.Literal["google-meet", "msteams", "zoom"],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DisconnectConferencingAppOutputResponseDto:
        """
        Disconnect your conferencing application

        DELETE /v2/conferencing/{app}/disconnect

        Args:
            app: Conferencing application type
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.conferencing.disconnect(app="google-meet")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/conferencing/{app}/disconnect",
            auth_names=["bearerAuth"],
            cast_to=models.DisconnectConferencingAppOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ConferencingAppsOutputResponseDto:
        """
        List your conferencing applications

        GET /v2/conferencing

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.conferencing.list()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/v2/conferencing",
            auth_names=["bearerAuth"],
            cast_to=models.ConferencingAppsOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def list_1(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.GetDefaultConferencingAppOutputResponseDto:
        """
        Get your default conferencing application

        GET /v2/conferencing/default

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.conferencing.list_1()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/v2/conferencing/default",
            auth_names=["bearerAuth"],
            cast_to=models.GetDefaultConferencingAppOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def connect(
        self,
        *,
        app: typing_extensions.Literal["google-meet"],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ConferencingAppOutputResponseDto:
        """
        Connect your conferencing application

        POST /v2/conferencing/{app}/connect

        Args:
            app: Conferencing application type
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.conferencing.connect(app="google-meet")
        ```
        """
        return await self._base_client.request(
            method="POST",
            path=f"/v2/conferencing/{app}/connect",
            auth_names=["bearerAuth"],
            cast_to=models.ConferencingAppOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def default(
        self,
        *,
        app: typing_extensions.Literal["daily-video", "google-meet", "msteams", "zoom"],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SetDefaultConferencingAppOutputResponseDto:
        """
        Set your default conferencing application

        POST /v2/conferencing/{app}/default

        Args:
            app: Conferencing application type
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.conferencing.default(app="daily-video")
        ```
        """
        return await self._base_client.request(
            method="POST",
            path=f"/v2/conferencing/{app}/default",
            auth_names=["bearerAuth"],
            cast_to=models.SetDefaultConferencingAppOutputResponseDto,
            request_options=request_options or default_request_options(),
        )
