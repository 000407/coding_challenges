def solution(a):
    instances = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    
    for num in a:
        for n in str(num):
            instances[n] = instances[n] + 1
    
    counts_max_digits = []
    max_count = 0
    
    for k, v in instances.items():
        if (v > max_count):
            max_count = v
            counts_max_digits = [int(k)]
        elif (v == max_count):
            counts_max_digits.append(int(k))
        else:
            pass
    
    return counts_max_digits

