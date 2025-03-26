
### get <a name="get"></a>
Get my profile



**API Endpoint**: `GET /v2/me`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.me.get()
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.me.get()
```

### patch <a name="patch"></a>
Update my profile



**API Endpoint**: `PATCH /v2/me`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.me.patch(
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
res = await client.me.patch(
    avatar_url="https://cal.com/api/avatar/2b735186-b01b-46d3-87da-019b8f61776b.png",
    locale_field="en",
    time_format=12.0,
    week_start="Monday",
)
```
