import typing

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
from calcom_py.types import models


class ManagedUsersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        client_id: str,
        limit: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        offset: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetManagedUsersOutput:
        """
        GET /v2/oauth-clients/{clientId}/managed-users

        Args:
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
        client.oauth_clients.managed_users.list(client_id="string")
        ```
        """
        _query: QueryParams = {}
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
            path=f"/v2/oauth-clients/{client_id}/managed-users",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetManagedUsersOutput,
            request_options=request_options or default_request_options(),
        )


class AsyncManagedUsersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        client_id: str,
        limit: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        offset: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetManagedUsersOutput:
        """
        GET /v2/oauth-clients/{clientId}/managed-users

        Args:
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
        await client.oauth_clients.managed_users.list(client_id="string")
        ```
        """
        _query: QueryParams = {}
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
            path=f"/v2/oauth-clients/{client_id}/managed-users",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetManagedUsersOutput,
            request_options=request_options or default_request_options(),
        )
