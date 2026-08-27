# t1 = (1, 'two', 3)
# t2 = (t1, 3.25)
# print(t2)
# print((t1 + t2))
# print((t1 + t2)[3])
# print((t1 + t2)[2:4])


# def intersect(t1, t2):
#     """Assumes t1 and t2 are tuples
#     Returns a tuple containing elements that are in
#     both t1 and t2"""
#     result = ()
#     for e in t1:
#         if e in t2:
#             result += (e,)
#     return result

# print(intersect((1, 'a', 2), ('b', 2, 'a')))



# a, b, c = 'xyz'
# print(a)



# def find_extreme_divisors(n1, n2):
#     """Assumes that n1 and n2 are positive ints
#     Returns a tuple containing the smallest common
#     divisor > 1 and
#     the largest common divisor of n1 & n2. If no
#     common divisor,
#     other than 1, returns (None, None)"""
#     min_val, max_val = None, None
#     for i in range(2, min(n1, n2) + 1):
#         if n1%i == 0 and n2%i == 0:
#             if min_val == None:
#                 min_val = i
#             max_val = i
#     return min_val, max_val

# print(find_extreme_divisors(24, 12))

# numbers = (1, 2, 3, 4, 5)
# mean = sum(numbers) / len(numbers)
# print(mean) 



# Techs = ['MIT', 'Caltech']
# Ivys = ['Harvard', 'Yale', 'Brown']

# Univs = [Techs, Ivys]
# Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]

# print(Univs == Univs1) #test value equality
# print(id(Univs) == id(Univs1)) #test object equality
# print(Univs is Univs1) #test object equality
# print('Id of Univs =', id(Univs))
# print('Id of Univs1 =', id(Univs1))

# Techs.append('RPI')
# Univs1[0].append('RPI')

# print(Techs)
# print(Univs)
# print(Univs1)


# L1 = [[]]*2
# L2 = [[], []]
# print(L1)
# print(L2)
# for i in range(len(L1)):
#     L1[i].append(i)
#     L2[i].append(i)
#     print('L1 =', L1, 'but', 'L2 =', L2)

# L = [1, 2, 3]
# L.append(L)
# print(L is L[-1])
# print(L[3])

# L = [1, 2]
# def append_val(val, list_1 = []):
#    list_1.append(val)
#    print(list_1)

# append_val(3, L)
# append_val(4)



# L1 = [1,2,3]
# L2 = [4,5,6]
# L3 = L1 + L2
# print('L3 =', L3)
# L1.extend(L2)
# print('L1 =', L1)
# L1.append(L2)
# print('L1 =', L1)



# def remove_dups(L1, L2):
#     """Assumes that L1 and L2 are lists.
#     Removes any element from L1 that also occurs in L2"""
#     for e1 in L1:
#         if e1 in L2:
#             L1.remove(e1)
# L1 = [1,2,3,4]
# L2 = [1,2,5,6]
# remove_dups(L1, L2)
# print('L1 =', L1)
# print(L2)

# non_primes = [x for x in range(2, 101) if any(x % i == 0 for i in range(2, int(x**0.5) + 1))]
non_primes = []
for x in range(2, 101):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            non_primes.append(x)
            break
print(non_primes)
