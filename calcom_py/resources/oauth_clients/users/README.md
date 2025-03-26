
### delete <a name="delete"></a>
Delete a managed user



**API Endpoint**: `DELETE /v2/oauth-clients/{clientId}/users/{userId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.oauth_clients.users.delete(client_id="string", user_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.oauth_clients.users.delete(client_id="string", user_id=123.45)
```

### list <a name="list"></a>
Get all managed users



**API Endpoint**: `GET /v2/oauth-clients/{clientId}/users`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.oauth_clients.users.list(client_id="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.oauth_clients.users.list(client_id="string")
```

### get <a name="get"></a>
Get a managed user



**API Endpoint**: `GET /v2/oauth-clients/{clientId}/users/{userId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.oauth_clients.users.get(client_id="string", user_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.oauth_clients.users.get(client_id="string", user_id=123.45)
```

### patch <a name="patch"></a>
Update a managed user



**API Endpoint**: `PATCH /v2/oauth-clients/{clientId}/users/{userId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.oauth_clients.users.patch(
    client_id="string",
    user_id=123.45,
    avatar_url="https://cal.com/api/avatar/2b735186-b01b-46d3-87da-019b8f61776b.png",
    locale_field="en",
    time_format=12.0,
    week_start="Monday",
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.oauth_clients.users.patch(
    client_id="string",
    user_id=123.45,
    avatar_url="https://cal.com/api/avatar/2b735186-b01b-46d3-87da-019b8f61776b.png",
    locale_field="en",
    time_format=12.0,
    week_start="Monday",
)
```

### create <a name="create"></a>
Create a managed user



**API Endpoint**: `POST /v2/oauth-clients/{clientId}/users`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.oauth_clients.users.create(
    client_id="string",
    email_field="alice@example.com",
    name="Alice Smith",
    avatar_url="https://cal.com/api/avatar/2b735186-b01b-46d3-87da-019b8f61776b.png",
    locale_field="en",
    time_format=12.0,
    time_zone="America/New_York",
    week_start="Monday",
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.oauth_clients.users.create(
    client_id="string",
    email_field="alice@example.com",
    name="Alice Smith",
    avatar_url="https://cal.com/api/avatar/2b735186-b01b-46d3-87da-019b8f61776b.png",
    locale_field="en",
    time_format=12.0,
    time_zone="America/New_York",
    week_start="Monday",
)
```
