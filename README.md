## Overview
Deep Research is an openai inspired tool, where you enter a prompt and the AI will research, taking anywhere from 5 to 30 mins conducting a thorough research on the prompt. This seems **awesome** but with openai's deep research, you can only have 5 researches for free without having to pay. You only need a few things to run this version of deep research.

## Prerequisites
- Cohere API key --> This is **free**. [Click here](https://cohere.com)
- Google Search API --> This is **free** [Follow the instructions here](https://developers.google.com/custom-search/v1/overview)
- Google Search Engine ID --> This is **free** [Click here](https://support.google.com/programmable-search/answer/12499034?hl=en)
- OpenAI API Key --> This is not free but it costs significantly less than paying for the plus or pro plan for chatgpt. [Click here](https://platform.openai.com/)

## Installation
Enter your API Keys into the .env file

Before you start, there are 2 files that you can run **app.py** or **main.py**. **main.py** is deep research in the command line with some interesting colors showing the different agents being used and the entire streamlined processes. But **app.py** is the same deep research but with a streamlit GUI.
#### Windows
```powershell
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
python main.py #For CLI
python app.py #For Streamlit GUI
```
#### MacOS / Linux
```zsh
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 main.py #For CLI
python3 app.py #For Streamlit GUI
```
