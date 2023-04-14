ASKBEND_BIN=askbend/target/release/askbend
CONF=conf/asknimo.toml

.PHONY: rebuild serve

all:

# rebuild
rebuild:
	$(ASKBEND_BIN) -c $(CONF) --rebuild

# serve
serve:
	$(ASKBEND_BIN) -c $(CONF)

### spider related

prepare-spider: spider/venv

spider/venv:
	@cd ./spider && python -m venv ./venv
	@./spider/venv/bin/pip install -r ./spider/requirements.txt

run-spider: spider/data

spider/data: spider/venv
	@cd ./spider && ./venv/bin/scrapy crawl nimo-wiki

### askbend related

prepare-askbend: askbend

askbend:
	@git submodule update --init --recursive

build-askbend: $(ASKBEND_BIN)

$(ASKBEND_BIN):
	@cd ./askbend && make build
