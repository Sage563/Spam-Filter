# Spam Filter

A Python-based CLI tool for fetching YouTube comments, detecting spam, analyzing sentiment, and computing discussion scores using state-of-the-art machine learning models.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Usage](#usage)
5. [Programmatic Usage](#programmatic-usage)
6. [Documentation](#documentation)
7. [File Structure](#file-structure)
8. [Contributing](#contributing)
9. [License](#license)

## Features
- **YouTube Comment Fetching**: Retrieve comments from any public YouTube video via the YouTube Data API, saving raw data to `video_data.json`.
- **Spam Detection**: Filter out spam using `AventIQ-AI/distilbert-spam-detection`, outputting full results in `fullresults.json` and non-spam comments in `spam_results.json`.
- **Sentiment Analysis**: Classify comment sentiment (Very Negative to Very Positive) with `tabularisai/multilingual-sentiment-analysis`, saving to `results.json`.
- **Scoring System**: Compute a weighted score and categorical rating (Poor, Fair, Good) based on sentiment.
- **Interactive CLI**: Guided prompts for URL input, comment count, and optional display of sentiment, score, and spam filter results.

## Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/spam_filter.git
   cd spam_filter/spam_filter
   ```
2. **Create a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *If `requirements.txt` is not present, install manually:*
   ```bash
   pip install pytube google-api-python-client torch transformers
   ```

## Configuration
- **API Key**: Create `key.txt` in the project root containing your YouTube Data API key.
- **Default URL (optional)**: Place a YouTube video link in `link.txt` for quick testing.
- **Python Version**: Compatible with Python 3.8+.

## Usage
### Interactive CLI
```bash
python main.py
```
1. Enter a YouTube URL or type `exit`/`quit`.
2. Specify the number of comments to fetch.
3. Choose to display sentiment results and overall score.
4. Opt to run spam detection and view filtered comments.

### Run Modules Individually
- **Comments Only**: Fetch comments and save raw JSON
  ```bash
  python -m spam_filter.comments
  ```
- **Sentiment Analysis**:
  ```bash
  python -m spam_filter.model
  ```
- **Scoring**:
  ```bash
  python -m spam_filter.score
  ```
- **Spam Detection**:
  ```bash
  python -m spam_filter.mids
  ```

## Install for Useing
- **Download** :When in the Relase padge(latest) download zip.zip

-Extract
- **Before Running**:
- Go to spam_filter dicrectory from the download and edit "key.txt" and put your key
- Then your ready all bugs are fixed code in the file "YOUR CODE HERE.py"
## Programmatic Usage
Import and configure modules in your own code:

```python
from spam_filter.comments import Comment
from spam_filter.model import Model
from spam_filter.score import LoadDict_score
from spam_filter.mids import SpamDetector
from spam_filter.strip import strip_youtube_url
from spam_filter.load_dict import load, different_load

# Fetch comments
commenter = Comment(video=strip_youtube_url("https://www.youtube.com/watch?v=..."), comments=100)
texts = commenter.run()

# Analyze sentiment
model = Model()
model.run()
print(model.display_results())

# Compute score
scorer = LoadDict_score()
print(scorer.run(), scorer.rating())

# Detect spam
detector = SpamDetector()
non_spam = detector.run()
```

## Documentation
### `comments.py`
- **Class**: `Comment(video_id: str, comments: int)`
  - `get_video_info(url)`: Retrieve video metadata with Pytube.
  - `get_comments(api_key, max_results)`: Paginate through YouTube Data API.
  - `run()`: Save raw JSON (`video_data.json`) and return cleaned text list.

### `load_dict.py`
- **remove_html_tags(text) -> str**: Strip HTML tags.
- **load() -> List[str]**: Load and clean `video_data.json`.
- **different_load() -> List[str]**: Load non-spam comments from `spam_results.json`.

### `model.py`
- **Class**: `Model()`
  - `predict_sentiment(texts) -> List[str]`: Tokenize and infer.
  - `run()`: Save sentiment mapping to `results.json`.
  - `display_results() -> str`: Return JSON-formatted sentiment.

### `score.py`
- **Class**: `LoadDict_score()`
  - `run() -> str`: Compute weighted score from `results.json`.
  - `rating() -> str`: Map score to rating category.

### `mids.py`
- **Class**: `SpamDetector()`
  - `predict_spam()`: Label each comment.
  - `run()`: Filter out spam, save to `spam_results.json`, return non-spam list.

### `strip.py`
- **Function**: `strip_youtube_url(url) -> str`: Extract video ID or exit on invalid.

### `utills.py`
- **Function**: `remove_by_value(d, target_value) -> Dict`: Remove entries matching a value.

## File Structure
```plaintext
spam_filter/
├─ comments.py
├─ load_dict.py
├─ main.py
├─ model.py
├─ score.py
├─ mids.py
├─ strip.py
├─ utills.py
├─ key.txt
├─ link.txt
├─ video_data.json
├─ results.json
├─ spam_results.json
├─ fullresults.json
├─ requirements.txt
└─ README.md
```

## Contributing
Contributions welcome! Please fork, create a feature branch, and open a pull request.

## License
MIT License. See [LICENSE](LICENSE).

