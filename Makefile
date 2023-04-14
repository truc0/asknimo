all:

prepare-spider: spider/venv

spider/venv:
	@cd ./spider && python -m venv ./venv
	@./spider/venv/bin/pip install -r ./spider/requirements.txt

run-spider: spider/data

spider/data: spider/venv
	@cd ./spider && ./venv/bin/scrapy crawl nimo-wiki

.PHONY: clean
