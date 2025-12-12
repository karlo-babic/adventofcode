import math

with open('12_input.txt') as f:
    text = f.read()
    text_parts = text.split('\n\n')

    presents_text = [present.split('\n') for present in text_parts[:-1]]
    presents = []
    for present in presents_text:
        presents.append(present[1:])

    regions_text = text_parts[-1].split('\n')
    regions = []
    for region in regions_text:
        if region == '':
            continue
        region = region.split(' ')
        shape = (int(region[0].split('x')[0]), int(region[0].split('x')[1].split(':')[0]))
        counts = []
        for count in region[1:]:
            counts.append(int(count))
        regions.append({'shape': shape, 'counts': counts})

def present_area(i):
    area = 0
    for row in presents[i]:
        area += row.count('#')
    return area

sure_fit_count = 0
imposible_fit_count = 0
unknown_fit_count = 0
for region in regions:
    num_presents = sum(region['counts'])
    num_presents_fit_x = math.floor(region['shape'][0]/3)
    num_presents_fit_y = math.floor(region['shape'][1]/3)
    sure = num_presents_fit_x * num_presents_fit_y >= num_presents

    presents_area = sum([present_area(i) * p_count for i, p_count in enumerate(region['counts'])])
    total_area = region['shape'][0] * region['shape'][1]
    impossible = presents_area > total_area
    
    unknown = not (sure or impossible)
    
    if sure:
        sure_fit_count += 1
    if impossible:
        imposible_fit_count += 1
    if unknown:
        unknown_fit_count += 1

print(sure_fit_count, imposible_fit_count, unknown_fit_count)