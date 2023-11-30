import requests

class HttpRequestFactory:
    def get_request(self, url: str):
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f'Error status {response.status_code} -- {response.json()}')
        else:
            return {'status': response.status_code, 'response': response}

    def post_request(self, url: str, body: str):
        response = requests.post(url, json=body)
        return {'status': response.status_code, 'response': response}

    def delete_request(self, url: str):
        response = requests.delete(url)

        if response.status_code != 200:
            raise Exception(f'Error status {response.status_code} -- {response.json()}')
        else:
            return {'status': response.status_code, 'response': response}
