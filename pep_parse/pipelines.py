import csv
from datetime import datetime as dt

from scrapy.exceptions import DropItem

from pep_parse.settings import BASE_DIR, DT_FORMAT, RESULTS_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.status = {}

    def process_item(self, item, spider):
        try:
            key = item['status']
            self.status[key] = self.status.get(key, 0) + 1
        except DropItem:
            raise DropItem('Drop item {item} from item_pipeline')
        return item

    def close_spider(self, spider):
        time = dt.now().strftime(DT_FORMAT)
        path = BASE_DIR / RESULTS_DIR / f'status_summary_{time}.csv'
        with open(path, mode='w', encoding='utf-8') as file:
            writer = csv.writer(
                file, dialect='unix', quoting=csv.QUOTE_NONE, escapechar=',')
            writer.writerows(
                (
                    ('Status', 'Quantity'),
                    *self.status.items(),
                    ('Total', sum(self.status.values()))
                ))
