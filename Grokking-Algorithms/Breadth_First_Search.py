from collections import deque


def person_seller(name):
    return name[-1] == 'm'


def bf_search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_seller(person):
                print(person + ' is mango seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jony']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jony'] = []

print(bf_search('you'))
