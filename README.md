# sentiment-analysis

A GPTScript tool performing sentiment analysis of some given text or file

## Setup

```
# Clone this repo
git clone https://github.com/gptscript-ai/sentiment-analysis.git
cd sentiment-analysis

# Set up the venv
python3 -m venv .venv
source .venv/bin/activate

# Install the packages
pip3 install -r requirements.txt
```

## Usage

### Get sentiment from a string

```
gptscript sentiments.gpt --content "this is the best movie I have ever watched"
```

### Get sentiment from a text file

```
gptscript sentiments.gpt --file files/tv-not-worth-it.txt
```

### Get sentiment from a pdf file

```
gptscript sentiments.gpt --file files/great-phone.pdf
```
