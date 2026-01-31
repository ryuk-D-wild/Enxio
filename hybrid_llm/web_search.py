"""
Web Search Tool - For internet-assisted code generation
Only used when explicitly requested
"""

import requests
from bs4 import BeautifulSoup
from typing import List, Dict


class WebSearchTool:
    """Simple web search for documentation and examples."""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def search_duckduckgo(self, query: str, max_results: int = 5) -> List[Dict]:
        """Search using DuckDuckGo (no API key needed)."""
        try:
            url = f"https://html.duckduckgo.com/html/?q={query}"
            response = self.session.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            results = []
            for result in soup.find_all('div', class_='result')[:max_results]:
                title_elem = result.find('a', class_='result__a')
                snippet_elem = result.find('a', class_='result__snippet')
                
                if title_elem:
                    results.append({
                        'title': title_elem.get_text(strip=True),
                        'url': title_elem.get('href', ''),
                        'snippet': snippet_elem.get_text(strip=True) if snippet_elem else ''
                    })
            
            return results
        except Exception as e:
            print(f"Search error: {e}")
            return []
    
    def fetch_page(self, url: str) -> str:
        """Fetch and extract text from a webpage."""
        try:
            response = self.session.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove script and style elements
            for script in soup(['script', 'style']):
                script.decompose()
            
            # Get text
            text = soup.get_text()
            
            # Clean up
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            
            return text[:5000]  # Limit to 5000 chars
        except Exception as e:
            print(f"Fetch error: {e}")
            return ""
    
    def search_docs(self, library: str, topic: str) -> str:
        """Search for library documentation."""
        query = f"{library} {topic} documentation example"
        results = self.search_duckduckgo(query, max_results=3)
        
        if not results:
            return "No results found"
        
        output = f"## Search Results for '{library} {topic}':\n\n"
        for i, result in enumerate(results, 1):
            output += f"{i}. **{result['title']}**\n"
            output += f"   URL: {result['url']}\n"
            output += f"   {result['snippet']}\n\n"
        
        return output


def main():
    """Test web search."""
    print("Testing Web Search Tool...")
    
    search = WebSearchTool()
    
    # Test search
    results = search.search_docs("python", "async await")
    print(results)


if __name__ == "__main__":
    main()
