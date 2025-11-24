import json
from scraper.article_scraper import scrape_article

def main():
    print("News Article Scraper")
    print("--------------------")
    
    url = input("Enter the URL of the news article: ").strip()
    
    if not url:
        print("Error: URL cannot be empty.")
        return

    print(f"Scraping {url}...")
    article_data = scrape_article(url)
    
    output_file = "article.json"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(article_data, f, indent=4, ensure_ascii=False)
        print(f"Successfully saved article to {output_file}")
        print(f"Title: {article_data.get('title')}")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()
