# GPS-using-MapQuest-API
implemented with Python 3

## The program

The program will describe a trip taken between a sequence of locations, the goal being to travel from the first location to the second, then from the second location to the third, and so on, until reaching the last location. Based on the user's input, it will show different information about the trip, such as turn-by-turn directions, distances and times, etc.  

## The input

The program will take input in the following format. It should not prompt the user in any way; it should simply read whatever input is typed into the console, and you should assume that your user knows the precise input format.  

- An integer whose value is at least 2, alone on a line, that specifies how many locations the trip will consist of.   
- If there are n locations, the next n lines of input will each describe one location. Each location can be a city such as Irvine, CA, an address such as 4545 Campus Dr, Irvine, CA, or anything that the Open MapQuest API will accept as a location. (The details of what is acceptable as a location is described here. Your program won't need to validate this input, but you'll need to expect that you might not get a valid response if you use something that MapQuest won't accept; you'll need to experiment with the Open MapQuest API's to see how they respond to invalid locations.)  
- A positive integer (i.e., whose value is at least 1), alone on a line, that specifies how many outputs will need to be generated.  
- If there are m outputs, the next m lines of input will each describe one output. Each output can be one of the following:  
  - STEPS for step-by-step directions, meaning a brief description of each maneuver (e.g., a turn, entering or exiting a freeway, etc.) you would have to make to drive from one location to another  
  - TOTALDISTANCE for the total distance traveled if completing the entire trip  
  - TOTALTIME for the total estimated time to complete the entire trip  
  - LATLONG for the latitude and longitude of each of the locations specified in the input  
  - ELEVATION for the elevation, in feet, of each of the locations specified in the input  

You can feel free to assume that the input will match the format described above; we will not be testing cases where it doesn't, so you can do anything you'd like — up to and including crashing — in such cases.  

## The output (when a route was found by MapQuest)  

After reading the input and processing it — downloading information from the MapQuest API, etc. — your program will generate the specified outputs in the forms described below. Each output must be preceded by a blank line, to set each one off from the others. The outputs must be written in the order that they were specified in the input (e.g., if the input said TOTALDISTANCE, then LATLONG, then TOTALTIME, the outputs must be shown in that order).  

- The STEPS output should begin with the word DIRECTIONS alone on a line, followed by one line of output for each maneuver that needs to be made along the path from the first location to the last.
- The TOTALDISTANCE output should be the words TOTAL DISTANCE, followed by a colon and a space, followed by the total distance (in an integer number of miles, rounded to the nearest mile) for the entire trip.
- The TOTALTIME output should be the words TOTAL TIME, followed by a colon and a space, followed by the total time (in an integer number of minutes, rounded to the nearest minute) that would be required to take the entire trip.
- The LATLONG output should be the word LATLONGS alone on a line, followed bby a latitude and longitude, one of each per line, for each of the locations specified in the input, in the order specified in the input. The latitude should come first, followed by a space, followed by the longitude.
  - The latitude's format is a number of degrees (formatted to two decimal places) followed by either N for north or S for south.
  - The longitude's format is a number of degrees (formatted to two decimal places) followed by either W for west or E for east.
- The ELEVATION output should be the word ELEVATIONS alone on a line, followed by an integer number of feet of elevation, one per line, for each of the locations specified in the input, in the order specified in the input. If MapQuest reports the elevation with a decimal part, round to the nearest integer.  

After the last output, print a blank line, and then the following copyright statement, alone on a line: Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.

## The output (when no route was found by MapQuest)

When no route was found by MapQuest — e.g., if you look for driving directions from Irvine, CA to Lisbon, Portugal, you won't find any — the program should simply output a blank line, followed by NO ROUTE FOUND alone on a line. This also includes the scenario where one or more of the locations was not valid (e.g., you looked for driving directions between locations that MapQuest did not recognize).  

## The output (when MapQuest returns some other kind of error)

When MapQuest returns another kind of error, other than a route not being found (e.g., the AppKey was invalid, you have no network connectivity, or MapQuest was down), the program should simply output a blank line, followed by MAPQUEST ERROR alone on a line.  

## An example of the program's execution

The following is an example of the program's execution, as it should be. Boldfaced, italicized text indicates input, while normal text indicates output.Note that the map data (the maneuvers, latitudes and longitudes, etc.) are hypothetical; I haven't taken them directly from MapQuest, since the goal of this example is to demonstrate the format.  
  
***3  
4533 Campus Dr, Irvine, CA  
1111 Figueroa St, Los Angeles, CA  
3799 S Las Vegas Blvd, Las Vegas, NV  
5  
LATLONG  
STEPS  
TOTALTIME  
TOTALDISTANCE  
ELEVATION***   
  
LATLONGS  
33.68N 117.77W  
34.02N 118.41W  
36.11N 115.17W  
  
DIRECTIONS  
West on Campus Dr.  
Right on Bristol  
CA-73 North  
Transition to I-405 North  
Transition to I-110 North  
Exit 9th Street  
South on S Figueroa St.  
Left on W 18th St.  
Enter I-10 East from W 18th St.  
Transition to I-15 North  
Exit S Las Vegas Blvd.  
  
TOTAL TIME: 317 minutes  
  
TOTAL DISTANCE: 365 miles  
  
ELEVATIONS  
542  
211  
2001  
  
Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors  
