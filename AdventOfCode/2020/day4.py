with open('day4.txt', 'r') as file:
    passports = file.read().split('\n\n')

required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
optional_field = 'cid'
count_part1 = 0
count_part2 = 0

for passport in passports:
    fields = passport.split()
    field_names = set()
    for field in fields:
        field_name = field.split(':')[0]
        field_names.add(field_name)

    if required_fields.issubset(field_names):
        count_part1 += 1

        # Part 2:
        field_data = {}
        for field in fields:
            field_name, field_value = field.split(':')
            field_data[field_name] = field_value

        
        if (
            1920 <= int(field_data['byr']) <= 2002 and
            2010 <= int(field_data['iyr']) <= 2020 and
            2020 <= int(field_data['eyr']) <= 2030 and
            ((field_data['hgt'].endswith('cm') and 150 <= int(field_data['hgt'][:-2]) <= 193) or
            (field_data['hgt'].endswith('in') and 59 <= int(field_data['hgt'][:-2]) <= 76)) and
            field_data['hcl'][0] == '#' and all(c in '0123456789abcdef' for c in field_data['hcl'][1:]) and
            field_data['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'} and
            len(field_data['pid']) == 9 and field_data['pid'].isdigit()
        ):
            count_part2 += 1

print("Part 1:", count_part1)
print("Part 2:", count_part2)

