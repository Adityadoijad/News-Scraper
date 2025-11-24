# 📰 News-Scraper

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight Python tool for extracting clean, structured content from news articles. Simply provide a URL, and News-Scraper will extract the article's title and body text, saving it to a JSON file for easy processing.

---

## ✨ Features

- 🎯 **Simple & Fast** - Extract article content with a single command
- 📄 **Clean Output** - Structured JSON format for easy integration
- 🔧 **Customizable** - Easy to modify for different HTML structures
- 🛡️ **Error Handling** - Gracefully handles malformed URLs and network errors
- 📦 **Minimal Dependencies** - Only uses essential libraries

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/News-Scraper.git
   cd News-Scrapper
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage

### Basic Usage

Run the scraper interactively:

```bash
python main.py
```

When prompted, enter the URL of the news article you want to scrape:

```
News Article Scraper
--------------------
Enter the URL of the news article: https://example.com/article
```

### Output

The scraped content will be saved to `article.json`:

```json
{
    "url": "https://example.com/article",
    "title": "Article Title Here",
    "content": "Full article text content..."
}
```

### Programmatic Usage

You can also import the scraper in your own Python scripts:

```python
from scraper.article_scraper import scrape_article

# Scrape an article
article_data = scrape_article("https://example.com/article")

# Access the data
print(article_data["title"])
print(article_data["content"])
```

---

## 📁 Project Structure

```
News-Scrapper/
├── scraper/
│   └── article_scraper.py    # Core scraping logic
├── main.py                    # CLI interface
├── requirements.txt           # Python dependencies
├── .gitignore                # Git ignore rules
├── LICENSE                    # MIT License
└── README.md                  # This file
```

---

## 🛠️ Technologies Used

- **[Requests](https://requests.readthedocs.io/)** - HTTP library for fetching web pages
- **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)** - HTML parsing and extraction
- **[lxml](https://lxml.de/)** - Fast XML/HTML parser

---

## 🎯 Use Cases

- 📊 **Content Aggregation** - Collect articles from multiple sources
- 📈 **Research & Analysis** - Extract data for sentiment analysis or NLP projects
- 🤖 **Automation** - Automatically archive important articles
- 📚 **Learning** - Study web scraping techniques

---

## ⚙️ Configuration

The scraper looks for:
- **Title**: `<h1>` tag
- **Content**: All `<p>` tags

To customize for different websites, modify `scraper/article_scraper.py`.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with Python and love ❤️
- Inspired by the need for simple, effective web scraping tools

---

## 📧 Contact

For questions, suggestions, or issues, please open an issue on GitHub.

**Happy Scraping! 🎉**
