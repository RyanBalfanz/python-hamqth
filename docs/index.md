---
layout: default
title: Documentation
---

HamQTH provides a simple interface for application developers.

`Python-HamQTH` provides a simple interface to querying the HamQTH XML callbook service.

## Installation

###  Install with Pip

```shell
pip install hamqth
```

### Install with Pipenv

```shell
pipenv install hamqth
```

## Usage

### Using `HamQTHClient`

#### Instantiate a new client

```python
>>> client = HamQTHClient()
```

If you have a session-id you can use it.

```python
>>> client = HamQTHClient(session_id='your-session-id')
```

#### Authenticate your client instance

```python
>>> client.authenticate('username', 'password')
```

Check if your client is authenticated.

```python
>>> client.is_authenticated
True
```

 This only checks for the existence of a session ID, it does not validate it. If the session ID is not valid, methods requiring authentication will fail.

##### Logout

```python
>>> client.logout()
>>> client.is_authenticated
False
```

#### Search for a callsign

Use the HamQTH XML callbook search with an authenticated client. If the callsign exists, an XML object is returned.

These methods require authentication. If the client is not authenticated, or if the session ID is invalid (e.g. expired), an exception will be raised.

##### Search callsign data

```python
>>> client.search_callsign('callsign')
```

##### Search callsign data with bio

```python
>>> client.search_callsign_bio('callsign')
```

##### Search callsign data with recent activity

```python
>>> client.search_callsign_recent_activity('callsign')
```
