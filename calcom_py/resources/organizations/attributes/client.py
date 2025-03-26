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
from calcom_py.resources.organizations.attributes.options import (
    AsyncOptionsClient,
    OptionsClient,
)
from calcom_py.types import models, params


class AttributesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.options = OptionsClient(base_client=self._base_client)

    def delete(
        self,
        *,
        attribute_id: str,
        org_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeleteOrganizationAttributesOutput:
        """
        Delete an attribute

        DELETE /v2/organizations/{orgId}/attributes/{attributeId}

        Args:
            attributeId: str
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.attributes.delete(attribute_id="string", org_id=123.0)
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/organizations/{org_id}/attributes/{attribute_id}",
            auth_names=["bearerAuth"],
            cast_to=models.DeleteOrganizationAttributesOutput,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        org_id: float,
        skip: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        take: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetOrganizationAttributesOutput:
        """
        Get all attributes

        GET /v2/organizations/{orgId}/attributes

        Args:
            skip: The number of items to skip
            take: The number of items to return
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.attributes.list(org_id=123.0)
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
            path=f"/v2/organizations/{org_id}/attributes",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetOrganizationAttributesOutput,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        attribute_id: str,
        org_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetSingleAttributeOutput:
        """
        Get an attribute

        GET /v2/organizations/{orgId}/attributes/{attributeId}

        Args:
            attributeId: str
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.attributes.get(attribute_id="string", org_id=123.0)
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/attributes/{attribute_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetSingleAttributeOutput,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        attribute_id: str,
        org_id: float,
        enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_field: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "MULTI_SELECT", "NUMBER", "SINGLE_SELECT", "TEXT"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.UpdateOrganizationAttributesOutput:
        """
        Update an attribute

        PATCH /v2/organizations/{orgId}/attributes/{attributeId}

        Args:
            enabled: bool
            name: str
            slug: str
            type: typing_extensions.Literal["MULTI_SELECT", "NUMBER", "SINGLE_SELECT", "TEXT"]
            attributeId: str
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.attributes.patch(attribute_id="string", org_id=123.0)
        ```
        """
        _json = to_encodable(
            item={
                "enabled": enabled,
                "name": name,
                "slug": slug,
                "type_field": type_field,
            },
            dump_with=params._SerializerUpdateOrganizationAttributeInput,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/v2/organizations/{org_id}/attributes/{attribute_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.UpdateOrganizationAttributesOutput,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        name: str,
        options: typing.List[params.CreateOrganizationAttributeOptionInput],
        org_id: float,
        slug: str,
        type_field: typing_extensions.Literal[
            "MULTI_SELECT", "NUMBER", "SINGLE_SELECT", "TEXT"
        ],
        enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateOrganizationAttributesOutput:
        """
        Create an attribute

        POST /v2/organizations/{orgId}/attributes

        Args:
            enabled: bool
            name: str
            options: typing.List[CreateOrganizationAttributeOptionInput]
            orgId: float
            slug: str
            type: typing_extensions.Literal["MULTI_SELECT", "NUMBER", "SINGLE_SELECT", "TEXT"]
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.attributes.create(
            name="string",
            options=[{"slug": "string", "value": "string"}],
            org_id=123.0,
            slug="string",
            type_field="MULTI_SELECT",
        )
        ```
        """
        _json = to_encodable(
            item={
                "enabled": enabled,
                "name": name,
                "options": options,
                "slug": slug,
                "type_field": type_field,
            },
            dump_with=params._SerializerCreateOrganizationAttributeInput,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/organizations/{org_id}/attributes",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreateOrganizationAttributesOutput,
            request_options=request_options or default_request_options(),
        )


class AsyncAttributesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.options = AsyncOptionsClient(base_client=self._base_client)

    async def delete(
        self,
        *,
        attribute_id: str,
        org_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeleteOrganizationAttributesOutput:
        """
        Delete an attribute

        DELETE /v2/organizations/{orgId}/attributes/{attributeId}

        Args:
            attributeId: str
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.attributes.delete(
            attribute_id="string", org_id=123.0
        )
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/organizations/{org_id}/attributes/{attribute_id}",
            auth_names=["bearerAuth"],
            cast_to=models.DeleteOrganizationAttributesOutput,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        org_id: float,
        skip: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        take: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetOrganizationAttributesOutput:
        """
        Get all attributes

        GET /v2/organizations/{orgId}/attributes

        Args:
            skip: The number of items to skip
            take: The number of items to return
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.attributes.list(org_id=123.0)
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
            path=f"/v2/organizations/{org_id}/attributes",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetOrganizationAttributesOutput,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        attribute_id: str,
        org_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetSingleAttributeOutput:
        """
        Get an attribute

        GET /v2/organizations/{orgId}/attributes/{attributeId}

        Args:
            attributeId: str
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.attributes.get(attribute_id="string", org_id=123.0)
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/attributes/{attribute_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetSingleAttributeOutput,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        attribute_id: str,
        org_id: float,
        enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_field: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "MULTI_SELECT", "NUMBER", "SINGLE_SELECT", "TEXT"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.UpdateOrganizationAttributesOutput:
        """
        Update an attribute

        PATCH /v2/organizations/{orgId}/attributes/{attributeId}

        Args:
            enabled: bool
            name: str
            slug: str
            type: typing_extensions.Literal["MULTI_SELECT", "NUMBER", "SINGLE_SELECT", "TEXT"]
            attributeId: str
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.attributes.patch(attribute_id="string", org_id=123.0)
        ```
        """
        _json = to_encodable(
            item={
                "enabled": enabled,
                "name": name,
                "slug": slug,
                "type_field": type_field,
            },
            dump_with=params._SerializerUpdateOrganizationAttributeInput,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/v2/organizations/{org_id}/attributes/{attribute_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.UpdateOrganizationAttributesOutput,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        name: str,
        options: typing.List[params.CreateOrganizationAttributeOptionInput],
        org_id: float,
        slug: str,
        type_field: typing_extensions.Literal[
            "MULTI_SELECT", "NUMBER", "SINGLE_SELECT", "TEXT"
        ],
        enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateOrganizationAttributesOutput:
        """
        Create an attribute

        POST /v2/organizations/{orgId}/attributes

        Args:
            enabled: bool
            name: str
            options: typing.List[CreateOrganizationAttributeOptionInput]
            orgId: float
            slug: str
            type: typing_extensions.Literal["MULTI_SELECT", "NUMBER", "SINGLE_SELECT", "TEXT"]
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.attributes.create(
            name="string",
            options=[{"slug": "string", "value": "string"}],
            org_id=123.0,
            slug="string",
            type_field="MULTI_SELECT",
        )
        ```
        """
        _json = to_encodable(
            item={
                "enabled": enabled,
                "name": name,
                "options": options,
                "slug": slug,
                "type_field": type_field,
            },
            dump_with=params._SerializerCreateOrganizationAttributeInput,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/organizations/{org_id}/attributes",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreateOrganizationAttributesOutput,
            request_options=request_options or default_request_options(),
        )
