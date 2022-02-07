

def get_numbers(src: list):
    result = [src[n + 1] for n in range(len(src) - 1) if src[n] < src[n + 1]]
    return result


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))




#src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#result = []
#for i in range(len(src)):
#    if len(src) > i + 1:
#        if src[i] < src[i + 1]:
            #result.append(src[i + 1])

#print(result)
