from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.onsite_subscription_create_query import OnsiteSubscriptionCreateQuery
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: OnsiteSubscriptionCreateQuery,
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
        "url": "/client/subscriptions/",
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
    body: OnsiteSubscriptionCreateQuery,
    company_id: str,
    revision: str = "2024-02-15",
) -> Response[Any]:
    """Create Client Subscription

     *Rate limits*:<br>Burst: `100/s`<br>Steady: `700/m`

    **Scopes:**
    `subscriptions:write`

    Args:
        company_id (str): Your Public API Key / Site ID. See [this
            article](https://help.klaviyo.com/hc/en-us/articles/115005062267) for more details.
            Example: PUBLIC_API_KEY.
        revision (str):  Default: '2024-02-15'.
        body (OnsiteSubscriptionCreateQuery):

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
    body: OnsiteSubscriptionCreateQuery,
    company_id: str,
    revision: str = "2024-02-15",
) -> Response[Any]:
    """Create Client Subscription

     *Rate limits*:<br>Burst: `100/s`<br>Steady: `700/m`

    **Scopes:**
    `subscriptions:write`

    Args:
        company_id (str): Your Public API Key / Site ID. See [this
            article](https://help.klaviyo.com/hc/en-us/articles/115005062267) for more details.
            Example: PUBLIC_API_KEY.
        revision (str):  Default: '2024-02-15'.
        body (OnsiteSubscriptionCreateQuery):

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
