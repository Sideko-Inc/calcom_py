
### disconnect <a name="disconnect"></a>
Disconnect your conferencing application



**API Endpoint**: `DELETE /v2/conferencing/{app}/disconnect`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.conferencing.disconnect(app="google-meet")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.conferencing.disconnect(app="google-meet")
```

### list <a name="list"></a>
List your conferencing applications



**API Endpoint**: `GET /v2/conferencing`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.conferencing.list()
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.conferencing.list()
```

### list_1 <a name="list_1"></a>
Get your default conferencing application



**API Endpoint**: `GET /v2/conferencing/default`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.conferencing.list_1()
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.conferencing.list_1()
```

### connect <a name="connect"></a>
Connect your conferencing application



**API Endpoint**: `POST /v2/conferencing/{app}/connect`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.conferencing.connect(app="google-meet")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.conferencing.connect(app="google-meet")
```

### default <a name="default"></a>
Set your default conferencing application



**API Endpoint**: `POST /v2/conferencing/{app}/default`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.conferencing.default(app="daily-video")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.conferencing.default(app="daily-video")
```
