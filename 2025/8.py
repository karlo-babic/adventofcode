import math

CONNECTIONS = 1000

with open('8_input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
points = []
for line in lines:
    points.append((int(line.split(',')[0]), int(line.split(',')[1]), int(line.split(',')[2])))

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)
distance_matrix = []
for p1 in points:
    row = []
    for p2 in points:
        row.append(distance(p1, p2))
    distance_matrix.append(row)

point_pairs = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        point_pairs.append((distance_matrix[i][j], (i, j)))
sorted_point_pairs = sorted(point_pairs, key=lambda x: x[0])

def in_which_cluster(id, clusters):
    for i in range(len(clusters)):
        if id in clusters[i]:
            return i
    return -1

connections_counter = 0
clusters = []
for point_pair in sorted_point_pairs:
    if connections_counter == CONNECTIONS:
        break
    c0 = in_which_cluster(point_pair[1][0], clusters)
    c1 = in_which_cluster(point_pair[1][1], clusters)
    if c0 == -1 and c1 == -1:
        clusters.append(set([point_pair[1][0], point_pair[1][1]]))
        connections_counter += 1
        print('new cluster:', points[point_pair[1][0]], points[point_pair[1][1]])
    elif c0 != -1 and c1 == -1:
        clusters[c0].add(point_pair[1][1])
        connections_counter += 1
        print('added to cluster:', points[point_pair[1][1]])
    elif c0 == -1 and c1 != -1:
        clusters[c1].add(point_pair[1][0])
        connections_counter += 1
        print('added to cluster:', points[point_pair[1][0]])
    elif c0 != c1:
        clusters[c0] = clusters[c0].union(clusters[c1])
        del clusters[c1]
        connections_counter += 1
        print('merged clusters')
    elif c0 == c1:
        connections_counter += 1
        print('same cluster')

def prod(nums):
    res = 1
    for val in nums:
        res = res * val
    return res

print()
top_clusters = sorted(clusters, key=lambda x: len(x), reverse=True)[:3]
print(prod([len(cluster) for cluster in top_clusters]))