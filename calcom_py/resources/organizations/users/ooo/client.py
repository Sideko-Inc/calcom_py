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
from calcom_py.types import params


class OooClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        ooo_id: float,
        org_id: float,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Delete ooo entry of a user

        DELETE /v2/organizations/{orgId}/users/{userId}/ooo/{oooId}

        Args:
            oooId: float
            orgId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.users.ooo.delete(ooo_id=123.0, org_id=123.0, user_id=123.0)
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/organizations/{org_id}/users/{user_id}/ooo/{ooo_id}",
            auth_names=["bearerAuth"],
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        org_id: float,
        user_id: float,
        skip: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        sort_end: typing.Union[
            typing.Optional[typing_extensions.Literal["asc", "desc"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        sort_start: typing.Union[
            typing.Optional[typing_extensions.Literal["asc", "desc"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        take: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Get all ooo entries of a user

        GET /v2/organizations/{orgId}/users/{userId}/ooo

        Args:
            skip: The number of items to skip
            sortEnd: Sort results by their end time in ascending or descending order.
            sortStart: Sort results by their start time in ascending or descending order.
            take: The number of items to return
            orgId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.users.ooo.list(org_id=123.0, user_id=123.0)
        ```
        """
        _query: QueryParams = {}
        if not isinstance(skip, type_utils.NotGiven):
            encode_query_param(
                _query,
                "skip",
                to_encodable(item=skip, dump_with=float),
                style="form",
                explode=True,
            )
        if not isinstance(sort_end, type_utils.NotGiven):
            encode_query_param(
                _query,
                "sortEnd",
                to_encodable(
                    item=sort_end, dump_with=typing_extensions.Literal["asc", "desc"]
                ),
                style="form",
                explode=True,
            )
        if not isinstance(sort_start, type_utils.NotGiven):
            encode_query_param(
                _query,
                "sortStart",
                to_encodable(
                    item=sort_start, dump_with=typing_extensions.Literal["asc", "desc"]
                ),
                style="form",
                explode=True,
            )
        if not isinstance(take, type_utils.NotGiven):
            encode_query_param(
                _query,
                "take",
                to_encodable(item=take, dump_with=float),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/users/{user_id}/ooo",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        ooo_id: float,
        org_id: float,
        user_id: float,
        end: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        notes: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        reason: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "public_holiday", "sick", "travel", "unspecified", "vacation"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        start: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        to_user_id: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Update ooo entry of a user

        PATCH /v2/organizations/{orgId}/users/{userId}/ooo/{oooId}

        Args:
            end: The end date and time of the out of office period in ISO 8601 format in UTC timezone.
            notes: Optional notes for the out of office entry.
            reason: the reason for the out of office entry, if applicable
            start: The start date and time of the out of office period in ISO 8601 format in UTC timezone.
            toUserId: The ID of the user covering for the out of office period, if applicable.
            oooId: float
            orgId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.users.ooo.patch(
            ooo_id=123.0,
            org_id=123.0,
            user_id=123.0,
            end="2023-05-10T23:59:59.999Z",
            notes="Vacation in Hawaii",
            reason="vacation",
            start="2023-05-01T00:00:00.000Z",
            to_user_id=2.0,
        )
        ```
        """
        _json = to_encodable(
            item={
                "end": end,
                "notes": notes,
                "reason": reason,
                "start": start,
                "to_user_id": to_user_id,
            },
            dump_with=params._SerializerUpdateOutOfOfficeEntryDto,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/v2/organizations/{org_id}/users/{user_id}/ooo/{ooo_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        end: str,
        org_id: float,
        start: str,
        user_id: float,
        notes: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        reason: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "public_holiday", "sick", "travel", "unspecified", "vacation"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        to_user_id: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Create an ooo entry for user

        POST /v2/organizations/{orgId}/users/{userId}/ooo

        Args:
            notes: Optional notes for the out of office entry.
            reason: the reason for the out of office entry, if applicable
            toUserId: The ID of the user covering for the out of office period, if applicable.
            end: The end date and time of the out of office period in ISO 8601 format in UTC timezone.
            orgId: float
            start: The start date and time of the out of office period in ISO 8601 format in UTC timezone.
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.users.ooo.create(
            end="2023-05-10T23:59:59.999Z",
            org_id=123.0,
            start="2023-05-01T00:00:00.000Z",
            user_id=123.0,
            notes="Vacation in Hawaii",
            reason="vacation",
            to_user_id=2.0,
        )
        ```
        """
        _json = to_encodable(
            item={
                "notes": notes,
                "reason": reason,
                "to_user_id": to_user_id,
                "end": end,
                "start": start,
            },
            dump_with=params._SerializerCreateOutOfOfficeEntryDto,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/organizations/{org_id}/users/{user_id}/ooo",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )


class AsyncOooClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        ooo_id: float,
        org_id: float,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Delete ooo entry of a user

        DELETE /v2/organizations/{orgId}/users/{userId}/ooo/{oooId}

        Args:
            oooId: float
            orgId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.users.ooo.delete(
            ooo_id=123.0, org_id=123.0, user_id=123.0
        )
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/organizations/{org_id}/users/{user_id}/ooo/{ooo_id}",
            auth_names=["bearerAuth"],
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        org_id: float,
        user_id: float,
        skip: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        sort_end: typing.Union[
            typing.Optional[typing_extensions.Literal["asc", "desc"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        sort_start: typing.Union[
            typing.Optional[typing_extensions.Literal["asc", "desc"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        take: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Get all ooo entries of a user

        GET /v2/organizations/{orgId}/users/{userId}/ooo

        Args:
            skip: The number of items to skip
            sortEnd: Sort results by their end time in ascending or descending order.
            sortStart: Sort results by their start time in ascending or descending order.
            take: The number of items to return
            orgId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.users.ooo.list(org_id=123.0, user_id=123.0)
        ```
        """
        _query: QueryParams = {}
        if not isinstance(skip, type_utils.NotGiven):
            encode_query_param(
                _query,
                "skip",
                to_encodable(item=skip, dump_with=float),
                style="form",
                explode=True,
            )
        if not isinstance(sort_end, type_utils.NotGiven):
            encode_query_param(
                _query,
                "sortEnd",
                to_encodable(
                    item=sort_end, dump_with=typing_extensions.Literal["asc", "desc"]
                ),
                style="form",
                explode=True,
            )
        if not isinstance(sort_start, type_utils.NotGiven):
            encode_query_param(
                _query,
                "sortStart",
                to_encodable(
                    item=sort_start, dump_with=typing_extensions.Literal["asc", "desc"]
                ),
                style="form",
                explode=True,
            )
        if not isinstance(take, type_utils.NotGiven):
            encode_query_param(
                _query,
                "take",
                to_encodable(item=take, dump_with=float),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/users/{user_id}/ooo",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        ooo_id: float,
        org_id: float,
        user_id: float,
        end: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        notes: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        reason: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "public_holiday", "sick", "travel", "unspecified", "vacation"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        start: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        to_user_id: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Update ooo entry of a user

        PATCH /v2/organizations/{orgId}/users/{userId}/ooo/{oooId}

        Args:
            end: The end date and time of the out of office period in ISO 8601 format in UTC timezone.
            notes: Optional notes for the out of office entry.
            reason: the reason for the out of office entry, if applicable
            start: The start date and time of the out of office period in ISO 8601 format in UTC timezone.
            toUserId: The ID of the user covering for the out of office period, if applicable.
            oooId: float
            orgId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.users.ooo.patch(
            ooo_id=123.0,
            org_id=123.0,
            user_id=123.0,
            end="2023-05-10T23:59:59.999Z",
            notes="Vacation in Hawaii",
            reason="vacation",
            start="2023-05-01T00:00:00.000Z",
            to_user_id=2.0,
        )
        ```
        """
        _json = to_encodable(
            item={
                "end": end,
                "notes": notes,
                "reason": reason,
                "start": start,
                "to_user_id": to_user_id,
            },
            dump_with=params._SerializerUpdateOutOfOfficeEntryDto,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/v2/organizations/{org_id}/users/{user_id}/ooo/{ooo_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        end: str,
        org_id: float,
        start: str,
        user_id: float,
        notes: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        reason: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "public_holiday", "sick", "travel", "unspecified", "vacation"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        to_user_id: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Create an ooo entry for user

        POST /v2/organizations/{orgId}/users/{userId}/ooo

        Args:
            notes: Optional notes for the out of office entry.
            reason: the reason for the out of office entry, if applicable
            toUserId: The ID of the user covering for the out of office period, if applicable.
            end: The end date and time of the out of office period in ISO 8601 format in UTC timezone.
            orgId: float
            start: The start date and time of the out of office period in ISO 8601 format in UTC timezone.
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.users.ooo.create(
            end="2023-05-10T23:59:59.999Z",
            org_id=123.0,
            start="2023-05-01T00:00:00.000Z",
            user_id=123.0,
            notes="Vacation in Hawaii",
            reason="vacation",
            to_user_id=2.0,
        )
        ```
        """
        _json = to_encodable(
            item={
                "notes": notes,
                "reason": reason,
                "to_user_id": to_user_id,
                "end": end,
                "start": start,
            },
            dump_with=params._SerializerCreateOutOfOfficeEntryDto,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/organizations/{org_id}/users/{user_id}/ooo",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )
