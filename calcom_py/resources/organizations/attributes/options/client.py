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


class OptionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete_from_user(
        self,
        *,
        attribute_option_id: str,
        org_id: float,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.UnassignOptionUserOutput:
        """
        Unassign an attribute from a user

        DELETE /v2/organizations/{orgId}/attributes/options/{userId}/{attributeOptionId}

        Args:
            attributeOptionId: str
            orgId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.attributes.options.delete_from_user(
            attribute_option_id="string", org_id=123.0, user_id=123.0
        )
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/organizations/{org_id}/attributes/options/{user_id}/{attribute_option_id}",
            auth_names=["bearerAuth"],
            cast_to=models.UnassignOptionUserOutput,
            request_options=request_options or default_request_options(),
        )

    def delete(
        self,
        *,
        attribute_id: str,
        option_id: str,
        org_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeleteAttributeOptionOutput:
        """
        Delete an attribute option

        DELETE /v2/organizations/{orgId}/attributes/{attributeId}/options/{optionId}

        Args:
            attributeId: str
            optionId: str
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.attributes.options.delete(
            attribute_id="string", option_id="string", org_id=123.0
        )
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/organizations/{org_id}/attributes/{attribute_id}/options/{option_id}",
            auth_names=["bearerAuth"],
            cast_to=models.DeleteAttributeOptionOutput,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        org_id: float,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetOptionUserOutput:
        """
        Get all attribute options for a user

        GET /v2/organizations/{orgId}/attributes/options/{userId}

        Args:
            orgId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.attributes.options.get(org_id=123.0, user_id=123.0)
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/attributes/options/{user_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetOptionUserOutput,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        attribute_id: str,
        org_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetAllAttributeOptionOutput:
        """
        Get all attribute options

        GET /v2/organizations/{orgId}/attributes/{attributeId}/options

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
        client.organizations.attributes.options.list(
            attribute_id="string", org_id=123.0
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/attributes/{attribute_id}/options",
            auth_names=["bearerAuth"],
            cast_to=models.GetAllAttributeOptionOutput,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        attribute_id: str,
        option_id: str,
        org_id: float,
        slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        value: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.UpdateAttributeOptionOutput:
        """
        Update an attribute option

        PATCH /v2/organizations/{orgId}/attributes/{attributeId}/options/{optionId}

        Args:
            slug: str
            value: str
            attributeId: str
            optionId: str
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.attributes.options.patch(
            attribute_id="string", option_id="string", org_id=123.0
        )
        ```
        """
        _json = to_encodable(
            item={"slug": slug, "value": value},
            dump_with=params._SerializerUpdateOrganizationAttributeOptionInput,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/v2/organizations/{org_id}/attributes/{attribute_id}/options/{option_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.UpdateAttributeOptionOutput,
            request_options=request_options or default_request_options(),
        )

    def create_to_user(
        self,
        *,
        attribute_id: str,
        org_id: float,
        user_id: float,
        attribute_option_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        value: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AssignOptionUserOutput:
        """
        Assign an attribute to a user

        POST /v2/organizations/{orgId}/attributes/options/{userId}

        Args:
            attributeOptionId: str
            value: str
            attributeId: str
            orgId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.attributes.options.create_to_user(
            attribute_id="string", org_id=123.0, user_id=123.0
        )
        ```
        """
        _json = to_encodable(
            item={
                "attribute_option_id": attribute_option_id,
                "value": value,
                "attribute_id": attribute_id,
            },
            dump_with=params._SerializerAssignOrganizationAttributeOptionToUserInput,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/organizations/{org_id}/attributes/options/{user_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.AssignOptionUserOutput,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        attribute_id: str,
        org_id: float,
        slug: str,
        value: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateAttributeOptionOutput:
        """
        Create an attribute option

        POST /v2/organizations/{orgId}/attributes/{attributeId}/options

        Args:
            attributeId: str
            orgId: float
            slug: str
            value: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.attributes.options.create(
            attribute_id="string", org_id=123.0, slug="string", value="string"
        )
        ```
        """
        _json = to_encodable(
            item={"slug": slug, "value": value},
            dump_with=params._SerializerCreateOrganizationAttributeOptionInput,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/organizations/{org_id}/attributes/{attribute_id}/options",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreateAttributeOptionOutput,
            request_options=request_options or default_request_options(),
        )


class AsyncOptionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete_from_user(
        self,
        *,
        attribute_option_id: str,
        org_id: float,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.UnassignOptionUserOutput:
        """
        Unassign an attribute from a user

        DELETE /v2/organizations/{orgId}/attributes/options/{userId}/{attributeOptionId}

        Args:
            attributeOptionId: str
            orgId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.attributes.options.delete_from_user(
            attribute_option_id="string", org_id=123.0, user_id=123.0
        )
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/organizations/{org_id}/attributes/options/{user_id}/{attribute_option_id}",
            auth_names=["bearerAuth"],
            cast_to=models.UnassignOptionUserOutput,
            request_options=request_options or default_request_options(),
        )

    async def delete(
        self,
        *,
        attribute_id: str,
        option_id: str,
        org_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeleteAttributeOptionOutput:
        """
        Delete an attribute option

        DELETE /v2/organizations/{orgId}/attributes/{attributeId}/options/{optionId}

        Args:
            attributeId: str
            optionId: str
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.attributes.options.delete(
            attribute_id="string", option_id="string", org_id=123.0
        )
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/organizations/{org_id}/attributes/{attribute_id}/options/{option_id}",
            auth_names=["bearerAuth"],
            cast_to=models.DeleteAttributeOptionOutput,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        org_id: float,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetOptionUserOutput:
        """
        Get all attribute options for a user

        GET /v2/organizations/{orgId}/attributes/options/{userId}

        Args:
            orgId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.attributes.options.get(org_id=123.0, user_id=123.0)
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/attributes/options/{user_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetOptionUserOutput,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        attribute_id: str,
        org_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetAllAttributeOptionOutput:
        """
        Get all attribute options

        GET /v2/organizations/{orgId}/attributes/{attributeId}/options

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
        await client.organizations.attributes.options.list(
            attribute_id="string", org_id=123.0
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/attributes/{attribute_id}/options",
            auth_names=["bearerAuth"],
            cast_to=models.GetAllAttributeOptionOutput,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        attribute_id: str,
        option_id: str,
        org_id: float,
        slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        value: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.UpdateAttributeOptionOutput:
        """
        Update an attribute option

        PATCH /v2/organizations/{orgId}/attributes/{attributeId}/options/{optionId}

        Args:
            slug: str
            value: str
            attributeId: str
            optionId: str
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.attributes.options.patch(
            attribute_id="string", option_id="string", org_id=123.0
        )
        ```
        """
        _json = to_encodable(
            item={"slug": slug, "value": value},
            dump_with=params._SerializerUpdateOrganizationAttributeOptionInput,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/v2/organizations/{org_id}/attributes/{attribute_id}/options/{option_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.UpdateAttributeOptionOutput,
            request_options=request_options or default_request_options(),
        )

    async def create_to_user(
        self,
        *,
        attribute_id: str,
        org_id: float,
        user_id: float,
        attribute_option_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        value: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AssignOptionUserOutput:
        """
        Assign an attribute to a user

        POST /v2/organizations/{orgId}/attributes/options/{userId}

        Args:
            attributeOptionId: str
            value: str
            attributeId: str
            orgId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.attributes.options.create_to_user(
            attribute_id="string", org_id=123.0, user_id=123.0
        )
        ```
        """
        _json = to_encodable(
            item={
                "attribute_option_id": attribute_option_id,
                "value": value,
                "attribute_id": attribute_id,
            },
            dump_with=params._SerializerAssignOrganizationAttributeOptionToUserInput,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/organizations/{org_id}/attributes/options/{user_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.AssignOptionUserOutput,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        attribute_id: str,
        org_id: float,
        slug: str,
        value: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateAttributeOptionOutput:
        """
        Create an attribute option

        POST /v2/organizations/{orgId}/attributes/{attributeId}/options

        Args:
            attributeId: str
            orgId: float
            slug: str
            value: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.attributes.options.create(
            attribute_id="string", org_id=123.0, slug="string", value="string"
        )
        ```
        """
        _json = to_encodable(
            item={"slug": slug, "value": value},
            dump_with=params._SerializerCreateOrganizationAttributeOptionInput,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/organizations/{org_id}/attributes/{attribute_id}/options",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreateAttributeOptionOutput,
            request_options=request_options or default_request_options(),
        )
