# L = ['I did it all', 4, 'love']

# for e in L:
#     print(e)

# L1 = [1, 2, 3]
# L2 = L1[-1::-1]
# print(L2)
# for i in range(len(L1)):
#     print(L1[i]*L2[i])

Techs = ['MIT', 'Caltech']
Ivys = ['Harvard', 'Yale', 'Brown']

Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]

# print('Univs =', Univs)
# print('Univs1 =', Univs1)
# print(Univs == Univs1)

# print(Univs == Univs1) #test value equality
# print(id(Univs) == id(Univs1)) #test object equality
# print(Univs is Univs1) #test object equality
# print('Id of Univs =', id(Univs))
# print('Id of Univs1 =', id(Univs1))

# print('Ids of Univs[0] and Univs[1]', id(Univs[0]),
# id(Univs[1]))
# print('Ids of Univs1[0] and Univs1[1]', id(Univs1[0]),
# id(Univs1[1]))

# Techs.append('RPI')
# print('Univs =', Univs)
# print('Univs1 =', Univs1)


# L1 = [[]]*2
# L2 = [[], []]
# for i in range(len(L1)):
#     L1[i].append(i)
#     L2[i].append(i)
# print('L1 =', L1, 'but', 'L2 =', L2)


# L = [1, 2, 3]
# L.append(L)
# print(L)
# print(L is L[-1])


# def append_val(val, list_1 = []):
#     list_1.append(val)
#     print(list_1)

# append_val(3)
# append_val(4)



# def apply_to_each(L, f):
#     """Assumes L is a list, f a function
#     Mutates L by replacing each element, e, of L by f(e)"""
#     for i in range(len(L)):
#         L[i] = f(L[i])

# L = [1, -2, 3.33]
# print('L =', L)
# print('Apply abs to each element of L.')
# apply_to_each(L, abs)
# print('L =', L)
# print('Apply int to each element of', L)
# apply_to_each(L, int)
# print('L =', L)
# print('Apply squaring to each element of', L)
# apply_to_each(L, lambda x: x**2)
# print('L =', L)


# print(list(map(int, range(10))))

# for i in map(lambda x: x**2, [2, 6, 4]):
#  print(i)

# L1 = [1, 28, 36]
# L2 = [2, 57, 9]
# for i in map(min, L1, L2):
#  print(i)

print('My favorite professor–John G.–rocks'.split(' '))
print('My favorite professor–John G.–rocks'.split('-'))
print('My favorite professor–John G.–rocks'.split('–'))
