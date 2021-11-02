# dictionary =  A changeable, unordered collection of unique key:value pairs
#                      Fast because they use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}

# print(capitals['Germany'])
# # you need the {} in order to update
# capitals.update({'Germany':'Berlin'})
# capitals.update({'USA':'Las Vegas'})
# capitals.pop('China')
# capitals.clear()

# print(capitals['Germany'])
# print(capitals.get('Germany'))
# # prints the keys
# print(capitals.keys())
# # prints the values
# print(capitals.values())
# # prints the keys and the values
# print(capitals.items())

for key, value in capitals.items():
    print(key, value)
