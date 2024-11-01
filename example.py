from src.aws_ipcollector.handler import AwsIpHandler

handler = AwsIpHandler(ranges_url="https://ip-ranges.amazonaws.com/ip-ranges.json", sqlite_path="aws.db")
handler.sync_prefixes()
db_prefixes = handler.get_prefixes()
print(db_prefixes[0].ip_prefix)