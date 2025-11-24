# News-Scraper

A simple Python-based tool that extracts the title and content of any news article when given its URL.

## Features
- Extracts article title (`<h1>`)
- Extracts article content (`<p>` tags)
- Saves output to `article.json`

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd News-Scrapper
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script:
```bash
python main.py
```

Enter the URL of the news article when prompted. The extracted data will be saved to `article.json`.
