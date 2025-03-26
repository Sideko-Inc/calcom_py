
### create <a name="create"></a>
Refresh API Key

Generate a new API key and delete the current one. Provide API key to refresh as a Bearer token in the Authorization header (e.g. "Authorization: Bearer <apiKey>").

**API Endpoint**: `POST /v2/api-keys/refresh`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.api_keys.refresh.create(
    api_key_days_valid=60.0, api_key_never_expires=True
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.api_keys.refresh.create(
    api_key_days_valid=60.0, api_key_never_expires=True
)
```
