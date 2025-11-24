import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    """
    Fetches the article at the given URL and extracts the title and content.
    
    Args:
        url (str): The URL of the news article.
        
    Returns:
        dict: A dictionary containing the 'url', 'title', and 'content'.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        soup = BeautifulSoup(response.content, 'lxml')
        
        # Extract title
        title_tag = soup.find('h1')
        title = title_tag.get_text(strip=True) if title_tag else "No Title Found"
        
        # Extract content (paragraphs)
        paragraphs = soup.find_all('p')
        content = "\n\n".join([p.get_text(strip=True) for p in paragraphs])
        
        return {
            "url": url,
            "title": title,
            "content": content
        }
    except Exception as e:
        return {
            "url": url,
            "title": "Error",
            "content": str(e)
        }
