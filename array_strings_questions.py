# implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def unique(string):
    for i in range(1, len(string)-1):
        if string[i] in string[1+i:] or string[i] in string[:i-1]:
            return -1
        else:
            continue
    return 1

# print(unique('qawzsexdrcftvgybhunjimkolp'))

def perm(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(0, len(str1)):
        print(i)
        if str1[i] in str2:
            found_index = str2.index(str1[i])
            if found_index ==0:
                str2 = str2[found_index+1:]
                print(str2)
                continue
            elif found_index == len(str1)-1:
                str2 = str2[:found_index]
                print(str2)
                
                continue
            else:
                str2 = str2[:found_index] + str2[found_index+1:]
                print(str2)
                
                continue
        else:
            return False
    return True

# print(perm('caasdbczx', 'zbaccasdz'))

def urlify(str1):
    for i in range(len(str1)):
        if str1[i] == " ":
            if i == 0:
                str1 = "%20" + str1[1:]
            elif i == len(str1)-1:
                str1 = str1[:i] + "%20"
            else:
                str1 = str1[:i] + "%20" + str1[i+1:]
        else:
            continue
    return str1

# print(urlify('this is a string'))

def palin(str1):
    pivot = False
    alpha = {}
    for i in range(len(str1)):
        if str1[i] in alpha:
            alpha[str1[i]]+=1
        else:
            alpha[str1[i]] = 1
    for j in alpha:
        if alpha[j] % 2 == 0:
            continue
        else:
            if pivot == False:
                pivot = True
            else:
                return False
    return True

print(palin('tactcoa'))