"""LangChain tool for Semantic Search"""

import requests
from langchain.tools import BaseTool

# the API allows limited use without a key
S2_API_KEY = ''

class SemanticSearch(BaseTool):
    name = "SemanticSearch"
    description = "Useful to find papers on about a tpoic"

    def _run(self, query: str) -> str:
        """Find papers on a topic"""

        result_limit = 10
        rsp = requests.get('https://api.semanticscholar.org/graph/v1/paper/search',
                           headers={'X-API-KEY': S2_API_KEY},
                           params={'query': query, 'limit': result_limit,
                                   'fields': 'title,url'})
        results = rsp.json()
        retval = []
        for idx, paper in enumerate(results['data']):
            retval.append(f'{idx}  {paper["title"]} {paper["url"]}')
        return ''.join(retval)


    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously"""
        raise NotImplementedError()


