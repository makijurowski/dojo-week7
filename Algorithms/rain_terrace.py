"""
This file is a submission for a Coding Dojo algorithm challenge.

CHALLENGE: Seattle Coding Dojo wants to send excess water to the Burbank
Coding Dojo by landscaping their rooftop with a set of unusual elevated
terraces. All terraces have the same width, but varying heights. When it
rains, water gathers in the low terraces that are surrounded by taller ones.
Given an array of rain_terrace heights, return the max amount of water
that can be trapped when it rains.

For example, if given an array of terraces with heights [3, 1, 1, 4, 2],
then the algorithm should identify that up to 4 units of water may be gathered.
"""


def find_all_terraces(terrace_list):
    rain_terrace = {'total_water': 0,
                    'bottom_vals': [],
                    'left_wall': 0,
                    'right_wall': 0, }
    for idx, val in enumerate(terrace_list, start=0):
        if rain_terrace['left_wall'] == 0:
            try:
                if (terrace_list[idx] > terrace_list[idx + 1] and
                        terrace_list[idx] > rain_terrace['left_wall']):
                    rain_terrace['left_wall'] = val
                    rain_terrace['left_idx'] = idx
            except:
                print('No water to be found!')
                return rain_terrace['total_water']
        elif rain_terrace['right_wall'] == 0:
            if idx == (len(terrace_list) - 1):
                rain_terrace['right_wall'] = val
                rain_terrace['right_idx'] = idx
            elif (terrace_list[idx] >= terrace_list[idx + 1] and
                  terrace_list[idx] > terrace_list[idx - 1]):
                rain_terrace['right_wall'] = val
                rain_terrace['right_idx'] = idx
        else:
            for i in range(rain_terrace['left_idx'] + 1, rain_terrace['right_idx']):
                rain_terrace['bottom_vals'].append(terrace_list[i])
            rain_terrace = gather_water(rain_terrace)
    if rain_terrace['left_wall'] != 0 and rain_terrace['right_wall'] != 0:
        for i in range(rain_terrace['left_idx'] + 1, rain_terrace['right_idx']):
            rain_terrace['bottom_vals'].append(terrace_list[i])
        rain_terrace = gather_water(rain_terrace)
    return rain_terrace['total_water']


def gather_water(rain_terrace):
    current_water = 0
    if rain_terrace['left_wall'] >= rain_terrace['right_wall']:
        lowest_wall = rain_terrace['right_wall']
    elif rain_terrace['left_wall'] < rain_terrace['right_wall']:
        lowest_wall = rain_terrace['left_wall']
    for val in rain_terrace['bottom_vals']:
        current_water += (lowest_wall - val)
    rain_terrace = {'total_water': rain_terrace['total_water'] + current_water,
                    'left_wall': rain_terrace['right_wall'],
                    'left_idx': rain_terrace['right_idx'],
                    'right_wall': 0,
                    'right_idx': 0,
                    'bottom_vals': [], }
    return rain_terrace


rain_terraces1 = [0, 1, 1, 0, 1]  # Expect 1
rain_terraces2 = [1, 1, 1, 3, 2, 1, 1, 3, 1]  # Expect 5
rain_terraces3 = [3, 1, 1, 4, 2]  # Expect 4
rain_terraces4 = [1, 2, 3, 2, 2, 4, 3, 2, 3, 4, 1, 2, 3, 4]  # Expect 12
rain_terraces5 = [0]  # Expect 0

"""TEST CASES"""
# print "Rain Terraces TC #1 (Expect = 1): "
print(find_all_terraces(rain_terraces1))
# print "Rain Terraces TC #2 (Expect = 5): "
print find_all_terraces(rain_terraces2)
# print "Rain Terraces TC #3 (Expect = 4): "
print find_all_terraces(rain_terraces3)
# print "Rain Terraces TC #4 (Expect = 12): "
print(find_all_terraces(rain_terraces4))
# print "Rain Terraces TC #5 (Expect = 0): "
print(find_all_terraces(rain_terraces5))
