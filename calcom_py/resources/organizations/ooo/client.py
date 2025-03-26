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


class OooClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        org_id: float,
        email_field: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
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
        Get all OOO entries of org users

        GET /v2/organizations/{orgId}/ooo

        Args:
            email: Filter ooo entries by the user email address. user must be within your organization.
            skip: The number of items to skip
            sortEnd: Sort results by their end time in ascending or descending order.
            sortStart: Sort results by their start time in ascending or descending order.
            take: The number of items to return
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.ooo.get(org_id=123.0)
        ```
        """
        _query: QueryParams = {}
        if not isinstance(email_field, type_utils.NotGiven):
            encode_query_param(
                _query,
                "email",
                to_encodable(item=email_field, dump_with=str),
                style="form",
                explode=True,
            )
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
            path=f"/v2/organizations/{org_id}/ooo",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )


class AsyncOooClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        org_id: float,
        email_field: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
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
        Get all OOO entries of org users

        GET /v2/organizations/{orgId}/ooo

        Args:
            email: Filter ooo entries by the user email address. user must be within your organization.
            skip: The number of items to skip
            sortEnd: Sort results by their end time in ascending or descending order.
            sortStart: Sort results by their start time in ascending or descending order.
            take: The number of items to return
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.ooo.get(org_id=123.0)
        ```
        """
        _query: QueryParams = {}
        if not isinstance(email_field, type_utils.NotGiven):
            encode_query_param(
                _query,
                "email",
                to_encodable(item=email_field, dump_with=str),
                style="form",
                explode=True,
            )
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
            path=f"/v2/organizations/{org_id}/ooo",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )
