from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_bis_subscription_create_query import ClientBISSubscriptionCreateQuery
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: ClientBISSubscriptionCreateQuery,
    company_id: str,
    revision: str = "2024-02-15",
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["revision"] = revision

    params: Dict[str, Any] = {}

    params["company_id"] = company_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/client/back-in-stock-subscriptions/",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.ACCEPTED:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.PAYMENT_REQUIRED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.METHOD_NOT_ALLOWED:
        return None
    if response.status_code == HTTPStatus.NOT_ACCEPTABLE:
        return None
    if response.status_code == HTTPStatus.PROXY_AUTHENTICATION_REQUIRED:
        return None
    if response.status_code == HTTPStatus.REQUEST_TIMEOUT:
        return None
    if response.status_code == HTTPStatus.CONFLICT:
        return None
    if response.status_code == HTTPStatus.GONE:
        return None
    if response.status_code == HTTPStatus.LENGTH_REQUIRED:
        return None
    if response.status_code == HTTPStatus.PRECONDITION_FAILED:
        return None
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        return None
    if response.status_code == HTTPStatus.REQUEST_URI_TOO_LONG:
        return None
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        return None
    if response.status_code == HTTPStatus.REQUESTED_RANGE_NOT_SATISFIABLE:
        return None
    if response.status_code == HTTPStatus.EXPECTATION_FAILED:
        return None
    if response.status_code == HTTPStatus.IM_A_TEAPOT:
        return None
    if response.status_code == HTTPStatus.MISDIRECTED_REQUEST:
        return None
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        return None
    if response.status_code == HTTPStatus.LOCKED:
        return None
    if response.status_code == HTTPStatus.FAILED_DEPENDENCY:
        return None
    if response.status_code == HTTPStatus.TOO_EARLY:
        return None
    if response.status_code == HTTPStatus.UPGRADE_REQUIRED:
        return None
    if response.status_code == HTTPStatus.PRECONDITION_REQUIRED:
        return None
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        return None
    if response.status_code == HTTPStatus.REQUEST_HEADER_FIELDS_TOO_LARGE:
        return None
    if response.status_code == HTTPStatus.UNAVAILABLE_FOR_LEGAL_REASONS:
        return None
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        return None
    if response.status_code == HTTPStatus.NOT_IMPLEMENTED:
        return None
    if response.status_code == HTTPStatus.BAD_GATEWAY:
        return None
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        return None
    if response.status_code == HTTPStatus.GATEWAY_TIMEOUT:
        return None
    if response.status_code == HTTPStatus.HTTP_VERSION_NOT_SUPPORTED:
        return None
    if response.status_code == HTTPStatus.VARIANT_ALSO_NEGOTIATES:
        return None
    if response.status_code == HTTPStatus.INSUFFICIENT_STORAGE:
        return None
    if response.status_code == HTTPStatus.LOOP_DETECTED:
        return None
    if response.status_code == HTTPStatus.NOT_EXTENDED:
        return None
    if response.status_code == HTTPStatus.NETWORK_AUTHENTICATION_REQUIRED:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ClientBISSubscriptionCreateQuery,
    company_id: str,
    revision: str = "2024-02-15",
) -> Response[Any]:
    """Create Client Back In Stock Subscription

     Subscribe a profile to receive back in stock notifications. Check out [our Back in Stock API
    guide](https://developers.klaviyo.com/en/docs/how_to_set_up_custom_back_in_stock) for more details.

    This endpoint is specifically designed to be called from publicly-browseable, client-side
    environments only. To create subscriptions from server-based applications, please use [POST
    /api/back-in-stock-subscriptions](https://developers.klaviyo.com/en/reference/create_back_in_stock_s
    ubscription).<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`

    **Scopes:**
    `catalogs:write`
    `profiles:write`

    Args:
        company_id (str): Your Public API Key / Site ID. See [this
            article](https://help.klaviyo.com/hc/en-us/articles/115005062267) for more details.
            Example: PUBLIC_API_KEY.
        revision (str):  Default: '2024-02-15'.
        body (ClientBISSubscriptionCreateQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        company_id=company_id,
        revision=revision,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ClientBISSubscriptionCreateQuery,
    company_id: str,
    revision: str = "2024-02-15",
) -> Response[Any]:
    """Create Client Back In Stock Subscription

     Subscribe a profile to receive back in stock notifications. Check out [our Back in Stock API
    guide](https://developers.klaviyo.com/en/docs/how_to_set_up_custom_back_in_stock) for more details.

    This endpoint is specifically designed to be called from publicly-browseable, client-side
    environments only. To create subscriptions from server-based applications, please use [POST
    /api/back-in-stock-subscriptions](https://developers.klaviyo.com/en/reference/create_back_in_stock_s
    ubscription).<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`

    **Scopes:**
    `catalogs:write`
    `profiles:write`

    Args:
        company_id (str): Your Public API Key / Site ID. See [this
            article](https://help.klaviyo.com/hc/en-us/articles/115005062267) for more details.
            Example: PUBLIC_API_KEY.
        revision (str):  Default: '2024-02-15'.
        body (ClientBISSubscriptionCreateQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        company_id=company_id,
        revision=revision,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
