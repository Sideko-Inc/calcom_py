
### get <a name="get"></a>
Get a provider



**API Endpoint**: `GET /v2/provider/{clientId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.provider.get(client_id="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.provider.get(client_id="string")
```

### verify_token <a name="verify_token"></a>
Verify an access token



**API Endpoint**: `GET /v2/provider/{clientId}/access-token`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.provider.verify_token(client_id="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.provider.verify_token(client_id="string")
```
