with open('day5.txt', 'r') as file:
    data = file.read().splitlines()
#print(data)

max_seat_id = 0
seat_ids = set()

for boarding_pass in data:
    row = int(boarding_pass[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(boarding_pass[7:].replace('L', '0').replace('R', '1'), 2)
    seat_id = row * 8 + col

    max_seat_id = max(max_seat_id, seat_id)
    seat_ids.add(seat_id)

print("Part 1:", max_seat_id)

# Part 2
missing_seat_id = None

for seat_id in range(1, max_seat_id):
    if seat_id not in seat_ids and seat_id - 1 in seat_ids and seat_id + 1 in seat_ids:
        missing_seat_id = seat_id

print("Part 2:", missing_seat_id)

