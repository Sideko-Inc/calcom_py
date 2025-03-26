
### create <a name="create"></a>
Force refresh tokens

If you have lost managed user access or refresh token, then you can get new ones by using OAuth credentials.
    Each access token is valid for 60 minutes and each refresh token for 1 year. Make sure to store them later in your database, for example, by updating the User model to have `calAccessToken` and `calRefreshToken` columns.

**API Endpoint**: `POST /v2/oauth-clients/{clientId}/users/{userId}/force-refresh`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.oauth_clients.users.force_refresh.create(
    client_id="string", user_id=123.45
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.oauth_clients.users.force_refresh.create(
    client_id="string", user_id=123.45
)
```
