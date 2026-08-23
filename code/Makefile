PYTHON ?= python3
VENV ?= .venv
PIP := $(VENV)/bin/pip
PY := $(VENV)/bin/python

APP := src/app.py
TEMPLATE := resources/cv-template.pdf
OUTPUT := build/user-cv.pdf
DATA_FILES := data/user-data-cv-1-data.json data/Job-details-data.json data/extra-form-data.json
RENDER_APP := src/app.py
RENDER_USER_INPUT_DIR := inputs/user
RENDER_SYSTEM_INPUT_DIR := inputs/system
RENDER_THEME ?= clean
RENDER_OUTPUT_HTML ?= build/generated_cv.html
RENDER_OUTPUT_PDF ?= build/generated_cv.pdf
RENDER_JOB_XML ?=

.PHONY: venv install fields lint test run build render-html render-pdf render-job clean

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r src/requirements.txt

fields: install
	$(PY) $(APP) --template $(TEMPLATE) --list-fields

lint: install
	$(PY) -m py_compile src/app.py tests/test_app.py

test: lint
	$(PY) -m unittest discover -s tests -v

run: install
	$(PY) $(APP) --template $(TEMPLATE) --output $(OUTPUT) --data-files $(DATA_FILES)

build: test run


render-html: install
	$(PY) $(RENDER_APP) html --user-input-dir $(RENDER_USER_INPUT_DIR) --system-input-dir $(RENDER_SYSTEM_INPUT_DIR) --output-html $(RENDER_OUTPUT_HTML) --theme $(RENDER_THEME)


render-pdf: install
	$(PY) $(RENDER_APP) html --user-input-dir $(RENDER_USER_INPUT_DIR) --system-input-dir $(RENDER_SYSTEM_INPUT_DIR) --output-html $(RENDER_OUTPUT_HTML) --theme $(RENDER_THEME) --output-pdf $(RENDER_OUTPUT_PDF)


render-job: install
	@if [ -z "$(RENDER_JOB_XML)" ]; then \
		echo "Error: set RENDER_JOB_XML, example: make render-job RENDER_JOB_XML=inputs/user/work-exp.xml"; \
		exit 1; \
	fi
	$(PY) $(RENDER_APP) html --user-input-dir $(RENDER_USER_INPUT_DIR) --system-input-dir $(RENDER_SYSTEM_INPUT_DIR) --output-html $(RENDER_OUTPUT_HTML) --theme $(RENDER_THEME) --job-xml $(RENDER_JOB_XML)

clean:
	rm -rf build .pytest_cache
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
