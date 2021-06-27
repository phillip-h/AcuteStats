# AcuteStats

This project is a set of small python modules intended for use by plugin authors
to track their plugin's usage statistics. There are currently two modules:

* `fetch.py` -- defines `get_stats(spigot_id, bstats_id, bstats_charts)`, which will return stats
for one or both of Spigot or bStats. See file for more information. This modules requires `urllib3`.
* `dynamo.py` -- defines `write_stats_to_dynamo(spigot_id, bstats_id, table)`, which will run `get_stats()`
with the given Spigot and bStats IDs then write the result to the provided DynamoDB table.
The table is assumed to be keyed on a string 'timestamp', this value is set to the current time when the ufunction is called.
This module requires `boto3`.

`lambda_function.py` additionally provides an example for how to use this project in an AWS Lambda function.

## About

AcuteStats was originally created by [zizmax](https://github.com/zizmax) and 
[phillip-h](https://github.com/phillip-h) for their plugin [AcuteLoot](https://github.com/zizmax/AcuteLoot)
