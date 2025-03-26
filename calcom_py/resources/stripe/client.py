import typing

from calcom_py.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
)
from calcom_py.resources.stripe.check import AsyncCheckClient, CheckClient
from calcom_py.resources.stripe.connect import AsyncConnectClient, ConnectClient
from calcom_py.types import models


class StripeClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.check = CheckClient(base_client=self._base_client)
        self.connect = ConnectClient(base_client=self._base_client)

    def save(
        self,
        *,
        code_field: str,
        state: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.StripCredentialsSaveOutputResponseDto:
        """
        Save stripe credentials

        GET /v2/stripe/save

        Args:
            code: str
            state: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.stripe.save(code_field="string", state="string")
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
            path="/v2/stripe/save",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.StripCredentialsSaveOutputResponseDto,
            request_options=request_options or default_request_options(),
        )


class AsyncStripeClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.check = AsyncCheckClient(base_client=self._base_client)
        self.connect = AsyncConnectClient(base_client=self._base_client)

    async def save(
        self,
        *,
        code_field: str,
        state: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.StripCredentialsSaveOutputResponseDto:
        """
        Save stripe credentials

        GET /v2/stripe/save

        Args:
            code: str
            state: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.stripe.save(code_field="string", state="string")
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
            path="/v2/stripe/save",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.StripCredentialsSaveOutputResponseDto,
            request_options=request_options or default_request_options(),
        )
