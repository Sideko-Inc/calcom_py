
### list <a name="list"></a>
GET /v2/oauth-clients/{clientId}/managed-users



**API Endpoint**: `GET /v2/oauth-clients/{clientId}/managed-users`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.oauth_clients.managed_users.list(client_id="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.oauth_clients.managed_users.list(client_id="string")
```
