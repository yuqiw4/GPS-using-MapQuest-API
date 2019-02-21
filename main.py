# Melody Wang 59907761
#user interface

import implements_outputs
import interacts_with_MapQuest


def num_of_locations() -> int:
    num_of_locations = int(input())
    return num_of_locations


def locations() -> list:
    locations = []
    n = num_of_locations()
    while n != 0:
        location = input()
        locations.append(location)
        n += -1
    return locations


def num_of_outputs() -> int:
    num_of_outputs = int(input())
    return num_of_outputs

def outputs() -> list:
    outputs = []
    n = num_of_outputs()
    while n != 0:
        output = input()
        try:
            result = implements_outputs.str_to_class(output)
            outputs.append(result)
            n += -1
        except:
            print('Invalid output type: ' + output)
            break
    return outputs


def main(locations: list, outputs: list) -> None:
    ends = locations[1:]
    direction_json = interacts_with_MapQuest.get_result(interacts_with_MapQuest.build_direction_url(locations[0],ends))
    try:
        if direction_json['info']['messages'] == ['We are unable to route with the given locations.']:
            print()
            print('NO ROUTE FOUND')

        list_of_elevation_url = interacts_with_MapQuest.build_elevation_url(direction_json)
        list_of_elevation_json = []
    
        for elevation_url in list_of_elevation_url:
            list_of_elevation_json.append(interacts_with_MapQuest.get_result(elevation_url))
        
        for output in outputs:
            try:
                x = output(direction_json)
                x.print_output()
            except:
                x = output(list_of_elevation_json)
                x.print_output()

        print()
        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')

    except:
        pass
    

if __name__ == '__main__':
    locations = locations()
    outputs = outputs()
    main(locations, outputs)




