from collections import deque

graph = {}
graph["you"] = [ "alice", 'bob', "claire"]
graph['bob'] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "johny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

l = ('claire', "anuj")

def person_is_seller(a):
    global l
    if a in l:
        return True
    else:
        return False


def search(name):
    search_queue = deque()
    search_queue += graph["you"]
    check = set()
    while search_queue:
        person = search_queue.popleft()
        if person not in check:
            if person_is_seller(person):
                print(person + ' ')
                return True
            else:
                search_queue += graph[person]
                check.add(person)
    return False

search('you')


