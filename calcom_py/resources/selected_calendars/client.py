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
from calcom_py.types import models, params


class SelectedCalendarsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        credential_id: str,
        external_id: str,
        integration: str,
        delegation_credential_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SelectedCalendarOutputResponseDto:
        """
        Delete a selected calendar

        DELETE /v2/selected-calendars

        Args:
            delegationCredentialId: str
            credentialId: str
            externalId: str
            integration: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.selected_calendars.delete(
            credential_id="string", external_id="string", integration="string"
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "credentialId",
            to_encodable(item=credential_id, dump_with=str),
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
            "integration",
            to_encodable(item=integration, dump_with=str),
            style="form",
            explode=True,
        )
        if not isinstance(delegation_credential_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "delegationCredentialId",
                to_encodable(item=delegation_credential_id, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="DELETE",
            path="/v2/selected-calendars",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.SelectedCalendarOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        credential_id: float,
        external_id: str,
        integration: str,
        delegation_credential_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SelectedCalendarOutputResponseDto:
        """
        Add a selected calendar

        POST /v2/selected-calendars

        Args:
            delegationCredentialId: str
            credentialId: float
            externalId: str
            integration: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.selected_calendars.create(
            credential_id=123.0, external_id="string", integration="string"
        )
        ```
        """
        _json = to_encodable(
            item={
                "delegation_credential_id": delegation_credential_id,
                "credential_id": credential_id,
                "external_id": external_id,
                "integration": integration,
            },
            dump_with=params._SerializerSelectedCalendarsInputDto,
        )
        return self._base_client.request(
            method="POST",
            path="/v2/selected-calendars",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.SelectedCalendarOutputResponseDto,
            request_options=request_options or default_request_options(),
        )


class AsyncSelectedCalendarsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        credential_id: str,
        external_id: str,
        integration: str,
        delegation_credential_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SelectedCalendarOutputResponseDto:
        """
        Delete a selected calendar

        DELETE /v2/selected-calendars

        Args:
            delegationCredentialId: str
            credentialId: str
            externalId: str
            integration: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.selected_calendars.delete(
            credential_id="string", external_id="string", integration="string"
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "credentialId",
            to_encodable(item=credential_id, dump_with=str),
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
            "integration",
            to_encodable(item=integration, dump_with=str),
            style="form",
            explode=True,
        )
        if not isinstance(delegation_credential_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "delegationCredentialId",
                to_encodable(item=delegation_credential_id, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="DELETE",
            path="/v2/selected-calendars",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.SelectedCalendarOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        credential_id: float,
        external_id: str,
        integration: str,
        delegation_credential_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SelectedCalendarOutputResponseDto:
        """
        Add a selected calendar

        POST /v2/selected-calendars

        Args:
            delegationCredentialId: str
            credentialId: float
            externalId: str
            integration: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.selected_calendars.create(
            credential_id=123.0, external_id="string", integration="string"
        )
        ```
        """
        _json = to_encodable(
            item={
                "delegation_credential_id": delegation_credential_id,
                "credential_id": credential_id,
                "external_id": external_id,
                "integration": integration,
            },
            dump_with=params._SerializerSelectedCalendarsInputDto,
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/selected-calendars",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.SelectedCalendarOutputResponseDto,
            request_options=request_options or default_request_options(),
        )
