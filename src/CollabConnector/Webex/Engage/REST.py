import requests
import sys
import json
import base64


class REST:
    def __init__(self, key, domain, base_url="https://chat-api.imi.chat"):
        self.key = key
        self.engage_domain = domain
        self.auth_code = base64.b64encode(f"{key}@{domain}".encode("ascii")).decode('UTF-8')
        self.base_url = base_url
        self.authenticate()

    def authenticate(self) -> str:
        try:
            token = requests.get(f"{self.base_url}/authorize",
                                 headers={"auth_code": self.auth_code,
                                          "Content-Type": "application/json"}
                                 ).headers['access_token']
        except Exception as err:
            raise Exception(f"Authentication Error: {str(err)}")
        else:
            return token

    def get(self, uri: str, params: dict = {}, headers: dict = {}, paging: bool = True) -> dict:
        uri = f"/{uri}" if uri.find('/') != 0 else uri
        if uri.find(self.base_url) > 0:
            uri = uri
        else:
            uri = f"{self.base_url}{uri}"

        headers.update({"access_token": self.authenticate(),
                        "Content-Type": "applicaton/json"})

        page = 0
        page_count = 1
        rest_response = None
        while page < page_count:
            page += 1
            try:
                response = requests.get(f"{uri}",
                                        headers=headers,
                                        data=params
                                        ).json()
            except Exception as err:
                print(f"GET ERROR: {uri} - {err}", file=sys.stderr)
                return {}
            else:
                if 'links' in response['response'].keys() and response['response']['links']['pages'] > page_count:
                    page_count = response['response']['links']['pages']
                if response['response'] is None:
                    print(f"REST GET Error: {uri} - {response['status_code']} - {response['description']}",
                          file=sys.stderr)
                    return {}
                if rest_response is None:
                    rest_response = response['response']
                else:
                    for key in rest_response:
                        if isinstance(rest_response[key], list):
                            rest_response[key].extend(response['response'][key])
                if page == page_count or paging is False:
                    return rest_response
                else:
                    uri = response['response']['links']['next']

    def post(self, uri: str, data: dict = {}, headers: dict = {}) -> dict:
        uri = f"/{uri}" if uri.find('/') != 0 else uri
        if uri.find(self.base_url) > 0:
            uri = uri
        else:
            uri = f"{self.base_url}{uri}"

        headers.update({"access_token": self.authenticate()})
        # "Content-Type": "applicaton/json"})

        try:
            response = requests.post(f"{uri}",
                                     headers=headers,
                                     json=data
                                     ).json()
        except Exception as err:
            print(f"POST ERROR: {uri} - {err}", file=sys.stderr)
        else:
            if 'response' not in response.keys() or response['response'] is None:
                print(f"REST POST Error: {uri} - {response} - {data}",
                      file=sys.stderr)
                return {}
            return response['response']

    def patch(self, uri: str, params: dict = {}, headers: dict = {}) -> dict:
        uri = f"/{uri}" if uri.find('/') != 0 else uri
        if uri.find(self.base_url) > 0:
            uri = uri
        else:
            uri = f"{self.base_url}{uri}"

        headers.update({"access_token": self.authenticate()})
        # "Content-Type": "applicaton/json"})

        try:
            response = requests.patch(f"{uri}",
                                      headers=headers,
                                      json=params
                                      ).json()
        except Exception as err:
            print(f"PATCH ERROR: {uri} - {err}", file=sys.stderr)
        else:
            if 'response' not in response.keys() or response['response'] is None:
                print(f"REST PATCH Error: {uri} - {response} - {params}",
                      file=sys.stderr)
                return {}
            return response['response']

    def put(self, uri: str, params: dict = {}, headers: dict = {}) -> dict:
        uri = f"/{uri}" if uri.find('/') != 0 else uri
        if uri.find(self.base_url) > 0:
            uri = uri
        else:
            uri = f"{self.base_url}{uri}"

        headers.update({"access_token": self.authenticate()})
        # "Content-Type": "applicaton/json"})

        try:
            response = requests.put(f"{uri}",
                                    headers=headers,
                                    json=params
                                    ).json()
        except Exception as err:
            print(f"PUT ERROR: {uri} - {err}", file=sys.stderr)
        else:
            if 'response' not in response.keys() or response['response'] is None:
                print(f"REST PUT Error: {uri} - {response} - {params}",
                      file=sys.stderr)
                return {}
            return response['response']
