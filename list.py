#delete
a = [4,73,67,38]
del a[1]
print([4,73,67,38], "          del a[1]         ", a) #[4, 67, 38]

#multiply
a = [4,73,67,38]
b = a*2
print(a, "          a*2              ", b) #[4, 73, 67, 38, 4, 73, 67, 38]

#addition
a = [4,73,67,38]
b = a + [8]
print(a, "          a+[8]            ", b)

#check if in array
a = [4,73,67,38]
b = 67 in a
print(a, "          b = 67 in a      ", b)

#reverse
a = [4,73,67,38]
b = a[::-1]
print(a, "          b = a[::-1]      ", b)

#offset access
a = [4,73,67,38]
b = a[3]
print(a, "          b = a[3]         ", b)

#negative access
a = [4,73,67,38]
b = a[-2]
print(a, "          a[-2]            ", b)

#access from
a = [4,73,67,38]
b = a[2:]
print(a, "          b = a[2:]        ",b)

#length
a = [4,73,67,38]
b = len(a)
print(a, "          b = len(a)       ",b)

#minimum
a = [4,73,67,38]
b = min(a)
print(a, "          b = min(a)       ",b)

#max
a = [4,73,67,38]
b = max(a)
print(a, "          b = max(a)       ",b)

#index
a = [4,73,67,38, 73]
b = a.index(73)
print(a, "      b = a.index(73)  ", b)

#count
a = [4,73,67,38, 73]
b = a.count(73)
print(a, "      b = a.count(73)  ", b)

#append element
a = [4,73,67,38, 73]
a.append(8)
print([4,73,67,38, 73], "      b.append(8)      ", b)

#append list
a = [4,73,67,38, 73]
a.append([8])
print([4,73,67,38, 73], "      a.append([8])    ", a)

#extend only list
a = [4,73,67,38, 73]
a.extend([8,8])
print([4,73,67,38, 73], "      a.extend([8,8])  ", a)

#remove
a = [4,73,67,38, 73]
a.remove(4)
print([4,73,67,38, 73], "      a.remove(4)      ", a)

#pop first use
a = [4,73,67,38, 73]
a.pop()
print([4,73,67,38, 73], "      a.pop()          ", a)


#slice middle
a = [4,73,67,38, 73]
b = a.pop()
print([4,73,67,38, 73], "      b = a.pop()      ", b)