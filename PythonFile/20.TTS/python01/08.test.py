def not_empty(s):
    return s and s.strip()

s=['A', '', 'B', None, 'C', ' ']
filter(not_empty, s)
print(s)