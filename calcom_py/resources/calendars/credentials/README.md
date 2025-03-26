
### create <a name="create"></a>
Sync credentials



**API Endpoint**: `POST /v2/calendars/{calendar}/credentials`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.calendars.credentials.create(calendar_field="apple")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.calendars.credentials.create(calendar_field="apple")
```
