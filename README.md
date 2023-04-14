# AskNIMO

An interactive chat robot inspired by [askbend](https://github.com/datafuselabs/askbend).

## TODO

- [ ] Data preprocessing
    - [ ] Replace image tag with url
    - [ ] Emit `:::` blocks annotation
    - [ ] Reform path of fetched data
- [ ] AskBend
    - [ ] Improve prompt

## Dependencies

- [askbend](https://github.com/datafuselabs/askbend)
- Python 3.10+
- Scrapy

## Build

### Clone the repository

```bash
git clone https://github.com/truc0/asknimo
cd asknimo
```

### Prepare data

Create a virtual environment and install dependencies

```bash
make prepare-spider
```

Fetch markdown content from NIMO wiki

```bash
make run-spider
```

The fetched data will be located in `spider/data`.

### Build askbend

Clone the [askbend](https://github.com/datafuselabs/askbend) project

```bash
make prepare-askbend
```

#### Install Rust dependencies

The [askbend](https://github.com/datafuselabs/askbend) project depends on some rust package, run the following command to setup building environment:

```bash
cd askbend
make setup
cd ..  # change directory back to asknimo root for further commands
```

#### Build

```bash
make build-askbend
```

### Config

An example configuration is provided in `conf/asknimo.toml.example`

```bash
cp conf/asknimo.toml.example conf/asknimo.toml
```

Replace `DSN` field with your databend configuration

## Run

### Upload data to databend

```bash
make rebuild
```

### Run backend server

```bash
make serve
```

