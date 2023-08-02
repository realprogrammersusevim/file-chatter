# File Chatter

Query your files using a search engine and LLM powered summarization.

## Setup

First install the Python dependencies.

```bash
cd file-chatter
python3 -m venv venv
venv/bin/activate
pip install -r requirements.txt
```

Next, you'll need to build an index of your documents that the search engine can
use in the background. The files will need to be in LLM readable text such as
Markdown or plaintext.

```bash
./index "path to your files with glob like myfiles/*.md"
```

Finally, get GGML model weights for the chat version of Llama 2 that
[llama.cpp](https://github.com/ggerganov/llama.cpp) can use.

## Usage

Run the query script with the path to the model file and what you want to search
for.

```bash
./query -m "path to GGML weights" "the meaning of life"
```

## TODO

- [ ] Support more filetypes than plaintext
- [ ] Improve search engine
