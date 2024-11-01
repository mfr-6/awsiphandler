## Example usage:

### Create an instance of AwsIpHandler:
```
>>> from src.aws_ipcollector.handler import AwsIpHandler
>>> handler = AwsIpHandler(ranges_url="https://ip-ranges.amazonaws.com/ip-ranges.json", sqlite_path="aws.db")
```
### You can get list of prefixes directly from AWS' page.
```
>>> prefixes = handler.get_prefixes(live_result=True)
>>> print(prefixes[0])
{'ip_prefix': '3.4.12.4/32', 'region': 'eu-west-1', 'service': 'AMAZON', 'network_border_group': 'eu-west-1'}
```

### You can store prefixes in SQLite3 DB - simply just sync prefixes. Handler will create DB if no DB is present.
```
>>> handler.sync_prefixes()
Bulk Insert, Model: Prefix... |################################| 7919/7919
```

### Once done - you can pull the prefixes directly from DB
```
>>> prefixes_from_db = handler.get_prefixes()
>>> len(prefixes_from_db)
7919
>>> print(prefixes_from_db[0].ip_prefix)
3.4.12.4/32
>>> print(prefixes_from_db[0].region)
eu-west-1
```

