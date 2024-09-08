

while True:
    length = float(input('Please enter room length in meters:'))
    width = float(input('Please enter room width in meters:'))

    room_sq_m = length * width

    tile_types = {'Ceramic':200, 'Porcelain':302, 'Marble':490, 'Granite':750, 'Terracotta':130}

    tile_selection = input("Please type in your desired tile type,Ceramic,Porcelain,Granite,Marble,Terracotta: ")

    tile_value =  (tile_types[tile_selection])

    total_cost = room_sq_m * tile_value

    break

print(f'The cost of your {tile_selection} tiles, for the {room_sq_m} sq/m room is: R{total_cost}')





