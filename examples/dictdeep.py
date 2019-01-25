from copy import deepcopy

d = {}
d['names'] = ['Albert', 'Bob']
c = d.copy(d)
dc = deepcopy(d)
d['name'].append('Clive')
c
dc
