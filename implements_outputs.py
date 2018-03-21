# Melody Wang 59907761



#steps

class STEPS:
    def __init__(self, json_result: 'json'):
        self._json_result = json_result

    def print_output(self):
        print()
        print('DIRECTIONS')
        for leg in self._json_result['route']['legs']:
            for maneuver in leg['maneuvers']:
                print(maneuver['narrative'])


#total distance

class TOTALDISTANCE:
    def __init__(self, json_result: 'json'):
        self._json_result = json_result

    def print_output(self):
        print()
        print('TOTAL DISTANCE: {:.0f} miles'.format(self._json_result['route']['distance']))


#total time

class TOTALTIME:
    def __init__(self, json_result: 'json'):
        self._json_result = json_result

    def print_output(self):
        print()
        time = self._json_result['route']['time']/60
        print('TOTAL TIME: {:.0f} minutes'.format(time))


#latlong

class LATLONG:
    def __init__(self, json_result: 'json'):
        self._json_result = json_result

    def print_output(self):
        print()
        print('LATLONGS')
        for item in self._json_result['route']['locations']:
            lat = item['latLng']['lat']
            lng = item['latLng']['lng']
            if lat > 0:
                dire1 = 'N'
            else:
                dire1 = 'S'
            if lng > 0:
                dire2 = 'E'
            else:
                dire2 = 'W'
            print('{:.2f}{} {:.2f}{}'.format(abs(lat),dire1,abs(lng),dire2))




#elevation

class ELEVATION:
    def __init__(self, list_of_elevation_json: list):
        self._list_of_elevation_json = list_of_elevation_json

    def print_output(self):
        elevations = []
        for elevation_json in self._list_of_elevation_json:
            elevations.append(elevation_json['elevationProfile'][0]['height'])
        print()
        print('ELEVATIONS')
        for elevation in elevations:
            print('{:.0f}'.format(elevation))



def str_to_class(s:str) -> 'class' :
    result = eval(s)
    return result



