# SysMonitor

Monitors system resources including Memory, CPU and Disk usage. These resources are monitored and stored locally. The can be queried through a Web API as detailed below:

## Installation

`python setup.py install`

## Usage

```
sysmonitor --help
```


## Web API Overview

The Web API provides a way to query on the monitored events of a certain `resource`. A `resource` can be one of `cpu`, `mem`, `disk`. A monitored event is in the form

```json
{
    "id": <int>,
    "timestamp": <string>,
    "stats": <json of available statistics on the resource>
}
```

### Get a list of recent activity
```
GET localhost:5000/api/v1/:resource
```
```
RETURNS

{
    page: <int>,
    length: <int>,
    events: [<event>]
}
```

#### Query Parameters

* `sort`: either `1` (descending) or `-1` (ascending) (default `1`)
* `page`: pagination starting at `0` (default `0`)
* `size`: how many events to receive (default `20`)

### Get last event
```
GET localhost:5000/api/v1/:resource/last
```
```
RETURNS <event>
```
