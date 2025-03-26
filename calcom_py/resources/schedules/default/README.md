
### list <a name="list"></a>
Get default schedule

Get the default schedule of the authenticated user.

**API Endpoint**: `GET /v2/schedules/default`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.schedules.default.list(cal_api_version="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.schedules.default.list(cal_api_version="string")
```
