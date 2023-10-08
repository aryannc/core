"""Application credentials platform for senz."""

from aiosenz import AUTHORIZATION_ENDPOINT, TOKEN_ENDPOINT

from homeassistant.components.application_credentials import AuthorizationServer

async def async_get_authorization_server() -> AuthorizationServer:
    """Return authorization server."""
    return AuthorizationServer(
        authorize_url=AUTHORIZATION_ENDPOINT,
        token_url=TOKEN_ENDPOINT,
    )
