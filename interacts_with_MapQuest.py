# Melody Wang 59907761

import json
import urllib.parse
import urllib.request


MAP_API_KEY = 'Fmjtd%7Cluu821u2n5%2Caw%3Do5-94a5h0'

BASE_MAP_URL = 'http://open.mapquestapi.com'





def build_direction_url(start: str, ends:list) -> str:
    parameters = [ ('key', MAP_API_KEY),('shapeFormat', 'raw'),('from', start)]
    for end in ends:
        parameters.append(('to', end))
    code = urllib.parse.urlencode(parameters).replace('%25', '%')
    
    return BASE_MAP_URL + '/directions/v2/route?' + code


def build_elevation_url(json_result: 'json') -> list:

    try:
        list_of_elevation_url = []
        
        for item in json_result['route']['locations']:
            collections = ''
            collections = collections + str(item['latLng']['lat']) + ',' + str(item['latLng']['lng'])
            parameters = [ ('key', MAP_API_KEY),('unit','f'),('latLngCollection', collections)]
            code = urllib.parse.urlencode(parameters).replace('%25', '%')
            list_of_elevation_url.append(BASE_MAP_URL + '/elevation/v1/profile?' + code)

        return list_of_elevation_url
    
    except:
        pass




def get_result(url: str) -> 'json':
    
    response = None

    try:
        
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    except:
        
        print()
        print('MAPQUEST ERROR')

    finally:

        if response != None:
            response.close()



    
