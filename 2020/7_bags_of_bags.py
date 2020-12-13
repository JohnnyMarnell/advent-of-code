import gzip, re, json, collections

contains = collections.defaultdict(dict)
contained_by = collections.defaultdict(dict)

rules = filter(gzip.open('inputs/7.gz').read().split('\n'))
for rule in gzip.open('inputs/7.gz').read().split('\n'):
    if re.match('contain no other', rule):
        continue
    rule = rule.split(' bags contain')
    for contained in re.findall('(\d) (.*?) bag', rule[1]):
        contained_by[contained[1]][rule[0]] = int(contained[0])
        contains[rule[0]][contained[1]] = int(contained[0])

def bfs(graph, queue, visited, node):
    visited.add(node)
    queue.append(node)
    while queue:
        next_node = queue.pop()
        for neighbor in graph[next_node].keys():
            visited.add(neighbor)
            queue.append(neighbor)

def dfs(graph, node):
    child_sum = 0
    for child in graph[node].keys():
        child_sum += graph[node][child] * dfs(graph, child)
    return 1 + child_sum
    
visited = set()
bfs(contained_by, [], visited, 'shiny gold')
print(len(visited) - 1)
print(dfs(contains, 'shiny gold') - 1)