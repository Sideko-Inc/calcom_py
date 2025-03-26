
### delete <a name="delete"></a>
Delete a selected calendar



**API Endpoint**: `DELETE /v2/selected-calendars`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.selected_calendars.delete(
    credential_id="string", external_id="string", integration="string"
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.selected_calendars.delete(
    credential_id="string", external_id="string", integration="string"
)
```

### create <a name="create"></a>
Add a selected calendar



**API Endpoint**: `POST /v2/selected-calendars`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.selected_calendars.create(
    credential_id=123.45, external_id="string", integration="string"
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.selected_calendars.create(
    credential_id=123.45, external_id="string", integration="string"
)
```
