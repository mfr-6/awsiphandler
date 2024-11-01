from src.aws_ipcollector.collector import AwsIpCollector
from src.aws_ipcollector.db import DbHandler
from src.aws_ipcollector.models import Prefix

class AwsIpHandler:
    def __init__(self, ranges_url: str, sqlite_path: str) -> None:
        self.collector = AwsIpCollector(url=ranges_url)
        self.dbhandler = DbHandler(sqlite_path)

    def sync_prefixes(self) -> None:
        self.dbhandler.purge_table(Prefix)
        prefixes = self.get_prefixes(live_result=True)
        self.dbhandler.bulk_insert(Prefix, prefixes)
   
    def get_prefixes(self, live_result: bool = False) -> list[dict]:
        if live_result:
            return self.collector.get_ranges().get("prefixes")
        else:
            return self.dbhandler.get_prefixes()
    
    def get_prefixes_by_region(self, region_name: str, live_result: bool = False):
        if live_result:
            return [ prefix for prefix in self.get_prefixes(live_result=True) if prefix.get("region") == region_name ]
        else:
            return self.dbhandler.get_prefixes_by_region(region_name)


