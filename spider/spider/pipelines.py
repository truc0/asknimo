# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
from pathlib import Path
from .settings import SAVE_TO_PATH


class SaveToFilePipeline:

    def open_spider(self, spider):
        Path(SAVE_TO_PATH).mkdir(exist_ok=True)

    def save_to_file(self, item):
        title = item.get('title')
        markdown = item.get('markdown')
        Path(SAVE_TO_PATH / f"{title}.md").write_text(markdown)

    def process_item(self, item, spider):
        self.save_to_file(item)
        return item
