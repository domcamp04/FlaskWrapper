import requests


class TVMazeAPI:
    def __init__(self):
        self.base_url = 'https://api.tvmaze.com'
        self.api_key = ''
        
    def _get(self, url, headers={}):
        response = requests.get(url, headers=headers)
        return response
    
    def _create_show_obj(self, data):
        show_id = data['id']
        title = data['name']
        img = data['image']['medium'] if data['image'] else None
        summary = data['summary']
        network = data['network']['name']
        show = TVShow(show_id, title, img, summary, network)
        return show
        
    def search_shows(self, query):
        url = self.base_url + f'/search/shows?q={query}'
        res = self._get(url)
        if res.status_code == 200:
            searched_shows = res.json()
            shows = [self._create_show_obj(show['show']) for show in searched_shows]
            return shows
        return res
    
    def get_show_info(self, show_id):
        url = self.base_url + f'/shows/{show_id}'
        res = self._get(url)
        if res.status_code == 200:
            data = res.json()
            show = self._create_show_obj(data)
            return show
        return res


class TVShow:
    def __init__(self, show_id, title, img, summary, network):
        self.id = show_id
        self.title = title
        self.image = img
        self.summary = summary
        self.network = network
        
    def __repr__(self):
        return f'<TV Show | {self.title}>'
    
    def __str__(self):
        return f'{self.id} - {self.title}'
    