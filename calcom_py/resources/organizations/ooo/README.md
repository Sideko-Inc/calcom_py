
### get <a name="get"></a>
Get all OOO entries of org users



**API Endpoint**: `GET /v2/organizations/{orgId}/ooo`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.ooo.get(org_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.ooo.get(org_id=123.45)
```
