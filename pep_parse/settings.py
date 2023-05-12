from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'
DT_FORMAT = '%Y-%m-%d_%H-%M-%S'
SPIDER_URL = 'peps.python.org'

BOT_NAME = 'pep_parse'
SPIDER_MODULE_NAME = BOT_NAME + '.spiders'

SPIDER_MODULES = [SPIDER_MODULE_NAME]
NEWSPIDER_MODULE = SPIDER_MODULE_NAME


ROBOTSTXT_OBEY = True

FEEDS = {
    RESULTS_DIR + '/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
