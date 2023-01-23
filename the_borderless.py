destinations = ["Paris,France", "Shanghai, China","Los Angeles, USA","Sao Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#Let's define the function that will get the index of our destination list
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

#Test of the function
#test1 = get_destination_index("Paris,France")
#test2 = get_destination_index("Los Angeles, USA")

#print(test1)
#print(test2)

def get_travel_location(traveler_destination):
    traveler_destination_index = test_traveler.index(traveler_destination)
    return traveler_destination_index

test_destination_index = get_travel_location('Shanghai, China')

print(test_destination_index)




