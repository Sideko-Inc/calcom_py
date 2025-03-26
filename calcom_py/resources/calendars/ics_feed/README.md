
### check <a name="check"></a>
Check an ICS feed



**API Endpoint**: `GET /v2/calendars/ics-feed/check`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.calendars.ics_feed.check()
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.calendars.ics_feed.check()
```

### save <a name="save"></a>
Save an ICS feed



**API Endpoint**: `POST /v2/calendars/ics-feed/save`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.calendars.ics_feed.save(
    urls=["https://cal.com/ics/feed.ics", "http://cal.com/ics/feed.ics"],
    read_only=False,
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.calendars.ics_feed.save(
    urls=["https://cal.com/ics/feed.ics", "http://cal.com/ics/feed.ics"],
    read_only=False,
)
```
