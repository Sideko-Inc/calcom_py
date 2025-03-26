
### delete <a name="delete"></a>
DELETE /v2/oauth-clients/{clientId}



**API Endpoint**: `DELETE /v2/oauth-clients/{clientId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.oauth_clients.delete(client_id="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.oauth_clients.delete(client_id="string")
```

### list <a name="list"></a>
GET /v2/oauth-clients



**API Endpoint**: `GET /v2/oauth-clients`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.oauth_clients.list()
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.oauth_clients.list()
```

### get <a name="get"></a>
GET /v2/oauth-clients/{clientId}



**API Endpoint**: `GET /v2/oauth-clients/{clientId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.oauth_clients.get(client_id="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.oauth_clients.get(client_id="string")
```

### patch <a name="patch"></a>
PATCH /v2/oauth-clients/{clientId}



**API Endpoint**: `PATCH /v2/oauth-clients/{clientId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.oauth_clients.patch(client_id="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.oauth_clients.patch(client_id="string")
```

### create <a name="create"></a>
POST /v2/oauth-clients



**API Endpoint**: `POST /v2/oauth-clients`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.oauth_clients.create(
    name="string", permissions=["*"], redirect_uris=["string"]
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.oauth_clients.create(
    name="string", permissions=["*"], redirect_uris=["string"]
)
```
