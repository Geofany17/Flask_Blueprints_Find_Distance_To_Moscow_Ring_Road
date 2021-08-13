from Exception import  InvalidKey, NothingFound, UnexpectedResponse

from typing import Tuple

import requests

class GEOCODER:
    """
    Yandex Geocoder API:
      First, enter the API Key.
      --> from Geocoder import GEOCODER
      --> geocoder = Geocder("your API_KEY")

      Finding coordinate
      (it returns tuple(float(latitude), float(longitude)))
      --> cordinates = geocoder.cordinates("your Address")

      Finding area cordinates
      (it returns lowerCordinate, upperCordinate)
      (each cordinate have tuple(float(latitude), float(longitude)))
      --> area_cordinates = geocodcer.area_cordinates("your Address")
            
      Finding Address
      (it returns string)
      --> Address = geocoder.Address(your_latitude,your_longitude) 
    """
    api_key: str

    def __init__(self, api_key: str):
        self.api_key = api_key

    def _request(self, Address: str) -> dict:
        response = requests.get(
                    "https://geocode-maps.yandex.ru/",
                    params = dict(format="json", apikey=self.api_key, geocode=Address, lang="en-US"),
        )

        if response.status_code == 200:
            return response.json()["response"]
        elif response.status_code == 403:
            raise InvalidKey()
        else:
            raise UnexpectedResponse(
                f"status_code={response.status_code}, body={response.content}"
            )
    
    def Coordinates(self, Address: str) -> Tuple[float]:
        
        data = self._request(Address)["GeoObjectCollection"]["featureMember"]

        if not data:
            raise NothingFound(f'Nothing found for "{Address}" not found')

        Coordinates = data[0]["GeoObject"]["Point"]["pos"]
        
        longitude, latitude = tuple(Coordinates.split(" "))

        return float(latitude), float(longitude)
        #return Coordinates

    def area_Coordinates(self,Address: str) -> Tuple[tuple]:
        data = self._request(Address)["GeoObjectCollection"]["featureMember"]

        if not data:
            raise NothingFound(f'Nothing found for "{Address}" not found')

        lowerCorner = data[0]["GeoObject"]["boundedBy"]["Envelope"]["lowerCorner"]
        upperCorner = data[0]["GeoObject"]["boundedBy"]["Envelope"]["upperCorner"]

        lower_longitude, lower_latitude = tuple(lowerCorner.split(" "))
        upper_longitude, upper_latitude = tuple(upperCorner.split(" "))

        lowerCoordinate = (float(lower_latitude),float(lower_longitude))
        upperCoordinate = (float(upper_latitude),float(upper_longitude))

        return lowerCoordinate,upperCoordinate

    def Address(self, latitude: float, longitude: float) -> str:

        got = self._request(f"{longitude},{latitude}")
        data = got["GeoObjectCollection"]["featureMember"]

        if not data:
            raise NothingFound(f'Nothing found for "{latitude} {longitude}"')

        return data[0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["text"]
