import scrapy
from scrapy.http.request.form import urljoin
from ..items import NIMOWikiFile


class NimoWikiSpider(scrapy.Spider):
    name = "nimo-wiki"
    DOMAIN = "nimo.sjtu.edu.cn"
    allowed_domains = ["nimo.sjtu.edu.cn"]
    start_urls = ['https://nimo.sjtu.edu.cn/wiki/user-manual/_source/']

    def parse(self, response):
        # parse content
        title = response.css('#article-title::text').get().strip()
        markdown = response.css('#article-container pre > code::text').get().strip()
        # Path(get_data_path() / f"{title}.md").write_text(markdown)
        yield NIMOWikiFile(title=title, markdown=markdown)
        # parse nav list
        next_urls = response.css('#article-breadcrumbs div.dropdown-menu a::attr(href)').getall()
        next_urls = next_urls[:-3]  # emit the last three, '浏览子文章', '在同级目录下创建', '在下一级目录下创建'
        next_urls = [f'{url}/_source/' for url in next_urls]
        yield from response.follow_all(next_urls, callback=self.parse)

