import typing

from calcom_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from calcom_py.types import models, params


class RefreshClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        api_key_days_valid: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        api_key_never_expires: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RefreshApiKeyOutput:
        """
        Refresh API Key

        Generate a new API key and delete the current one. Provide API key to refresh as a Bearer token in the Authorization header (e.g. "Authorization: Bearer <apiKey>").

        POST /v2/api-keys/refresh

        Args:
            apiKeyDaysValid: For how many days is managed organization api key valid. Defaults to 30 days.
            apiKeyNeverExpires: If true, organization api key never expires.
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.api_keys.refresh.create(
            api_key_days_valid=60.0, api_key_never_expires=True
        )
        ```
        """
        _json = to_encodable(
            item={
                "api_key_days_valid": api_key_days_valid,
                "api_key_never_expires": api_key_never_expires,
            },
            dump_with=params._SerializerRefreshApiKeyInput,
        )
        return self._base_client.request(
            method="POST",
            path="/v2/api-keys/refresh",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.RefreshApiKeyOutput,
            request_options=request_options or default_request_options(),
        )


class AsyncRefreshClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        api_key_days_valid: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        api_key_never_expires: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RefreshApiKeyOutput:
        """
        Refresh API Key

        Generate a new API key and delete the current one. Provide API key to refresh as a Bearer token in the Authorization header (e.g. "Authorization: Bearer <apiKey>").

        POST /v2/api-keys/refresh

        Args:
            apiKeyDaysValid: For how many days is managed organization api key valid. Defaults to 30 days.
            apiKeyNeverExpires: If true, organization api key never expires.
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.api_keys.refresh.create(
            api_key_days_valid=60.0, api_key_never_expires=True
        )
        ```
        """
        _json = to_encodable(
            item={
                "api_key_days_valid": api_key_days_valid,
                "api_key_never_expires": api_key_never_expires,
            },
            dump_with=params._SerializerRefreshApiKeyInput,
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/api-keys/refresh",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.RefreshApiKeyOutput,
            request_options=request_options or default_request_options(),
        )
