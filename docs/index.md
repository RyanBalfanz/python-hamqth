---
layout: default
title: Python-HamQTH
---

# Python-HamQTH

## Installation

Installing is easy with Pip.

```
pip install python-hamqth
```

Or, similarly easy with Pipenv.

```
pipenv install python-hamqth
```

## Usage

### Using `HamQTHClient`

#### Instantiate a new client

```
>>> client = HamQTHClient()
```

If you have a session-id you can use it.

```
>>> client = HamQTHClient(session_id='your-session-id')
```

#### Authenticate your client instance

```
>>> client.authenticate('username', 'password')
```

Check if your client is authenticated.

```
>>> client.is_authenticated
True
```

 This only checks for the existence of a session ID, it does not validate it. If the session ID is not valid, methods requiring authentication will fail.

##### Logout

```
>>> client.logout()
>>> client.is_authenticated
False
```

#### Search for a callsign

Use the HamQTH XML callbook search with an authenticated client. If the callsign exists, an XML object is returned.

These methods require authentication. If the client is not authenticated, or if the session ID is invalid (e.g. expired), an exception will be raised.

##### Search callsign data

```
>>> client.search_callsign('callsign')
```

##### Search callsign data with bio

```
>>> client.search_callsign_bio('callsign')
```

##### Search callsign data with recent activity

```
>>> client.search_callsign_recent_activity('callsign')
```
