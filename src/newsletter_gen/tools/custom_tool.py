from crewai.tools import BaseTool
from typing import Type
from exa_py import Exa
from datetime import datetime, timedelta
import os


class SearchAndContents(BaseTool):
    name: str = "Search and Contents Tool"
    description: str = (
        "Searches the web based on a search query for the latest results. Results are only from the last week. Uses the Exa API. This also returns the contents of the search results."
    )
    
    def _exa(self):
        return Exa(os.getenv('EXA_API_KEY'))

    def _run(self, search_query: str) -> str:
        exa = self._exa()
        date_cutoff = (datetime.now() - timedelta(weeks=1)).strftime('%Y-%m-%d')
        search_results = exa.search_and_contents(
            query=search_query,
            start_published_date=date_cutoff,
            use_autoprompt=True
        )
        return search_results

class FindSimilar(BaseTool):
    name: str = "Find Similar Tool"
    description: str = (
        "Searches for similar articles to a given article using the Exa API. Takes in a URL of the article."
    )
    
    def _exa(self):
        return Exa(os.getenv('EXA_API_KEY'))

    def _run(self, article_url: str) -> str:
        exa = self._exa()
        date_cutoff = (datetime.now() - timedelta(weeks=1)).strftime('%Y-%m-%d')
        search_results = exa.find_similar(
            url=article_url,
            start_published_date=date_cutoff
        )
        return search_results

class GetContents(BaseTool):
    name: str = "Get Contents Tool"
    description: str = (
        "Gets the contents of a specific article using the Exa API. Takes in the ID of the article in a list, like this: ['https://www.cnbc.com/2024/04/18/my-news-story']."
    )
    
    def _exa(self):
        return Exa(os.getenv('EXA_API_KEY'))

    def _run(self, article_ids: list) -> str:
        exa = self._exa()
        search_results = exa.get_contents(
            ids=article_ids
        )
        return search_results


if __name__=="__main__":
    """search_and_contents = SearchAndContents()
    search_results = search_and_contents._run("latest new about AI")
    print(search_results)"""

    """similar = FindSimilar()
    search_results = similar._run("https://www.nytimes.com/2024/12/24/technology/elon-musk-xai-funding.html")
    print(search_results)"""

    contents = GetContents()
    search_results = contents._run(["https://www.nytimes.com/2024/12/24/technology/elon-musk-xai-funding.html"])
    print(search_results)