s = 'hello'
i = 0
for c in s:
    print(i, c)
    i += 1

s = 'hello'

for i in range(len(s)):
    print(i, s[i])

s = 'hello'

# enumerate returns the index and
# the element
# enumerate is the tuple
# the first el, is the index
# the second el, is the element
for i, c in enumerate(s):
    print(i, c)