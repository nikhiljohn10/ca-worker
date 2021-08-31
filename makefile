deploy: build
	@poetry run python -m caworker \
		-t "$$TOKEN" \
		-l "./build/index.js" \
		-f "This is a finerprint" \
		-u "https://ca.internal"

build: clean
	@mkdir -p ./build
	@echo "/* This is an auto generated file. Do not edit this file */\n" > ./build/index.js
	@sed -e '1i\'$$'\n''function get_html() { return \`'  -e '$$a\'$$'\n''\`}' ./worker/index.html >> ./build/index.js
	@cat ./worker/worker.js >> ./build/index.js

clean:
	@rm -rf dist/ workers/ build/ caworker.egg-info/
	@find . -type d -name *pycache* -exec rm -rf {} +

.PHONY: clean build deploy