
### auth_url <a name="auth_url"></a>
Get OAuth conferencing app auth url



**API Endpoint**: `GET /v2/conferencing/{app}/oauth/auth-url`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.conferencing.oauth.auth_url(
    app="msteams", on_error_return_to="string", return_to="string"
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.conferencing.oauth.auth_url(
    app="msteams", on_error_return_to="string", return_to="string"
)
```

### callback <a name="callback"></a>
conferencing apps oauths callback



**API Endpoint**: `GET /v2/conferencing/{app}/oauth/callback`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.conferencing.oauth.callback(
    app="msteams", code_field="string", state="string"
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.conferencing.oauth.callback(
    app="msteams", code_field="string", state="string"
)
```
