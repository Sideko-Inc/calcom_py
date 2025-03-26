import typing

from calcom_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
)
from calcom_py.types import models, params


class OauthClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def refresh(
        self,
        *,
        client_id: str,
        refresh_token: str,
        x_cal_secret_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.KeysResponseDto:
        """
        Refresh managed user tokens

        If managed user access token is expired then get a new one using this endpoint. Each access token is valid for 60 minutes and
            each refresh token for 1 year. Make sure to store them later in your database, for example, by updating the User model to have `calAccessToken` and `calRefreshToken` columns.

        POST /v2/oauth/{clientId}/refresh

        Args:
            clientId: str
            refreshToken: Managed user's refresh token.
            x-cal-secret-key: OAuth client secret key.
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth.refresh(
            client_id="string", refresh_token="string", x_cal_secret_key="string"
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["x-cal-secret-key"] = str(x_cal_secret_key)
        _json = to_encodable(
            item={"refresh_token": refresh_token},
            dump_with=params._SerializerRefreshTokenInput,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/oauth/{client_id}/refresh",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.KeysResponseDto,
            request_options=request_options or default_request_options(),
        )


class AsyncOauthClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def refresh(
        self,
        *,
        client_id: str,
        refresh_token: str,
        x_cal_secret_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.KeysResponseDto:
        """
        Refresh managed user tokens

        If managed user access token is expired then get a new one using this endpoint. Each access token is valid for 60 minutes and
            each refresh token for 1 year. Make sure to store them later in your database, for example, by updating the User model to have `calAccessToken` and `calRefreshToken` columns.

        POST /v2/oauth/{clientId}/refresh

        Args:
            clientId: str
            refreshToken: Managed user's refresh token.
            x-cal-secret-key: OAuth client secret key.
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth.refresh(
            client_id="string", refresh_token="string", x_cal_secret_key="string"
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["x-cal-secret-key"] = str(x_cal_secret_key)
        _json = to_encodable(
            item={"refresh_token": refresh_token},
            dump_with=params._SerializerRefreshTokenInput,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/oauth/{client_id}/refresh",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.KeysResponseDto,
            request_options=request_options or default_request_options(),
        )
