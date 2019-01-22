#is my friend cheating

'''
def removNb(n):
    total = n*(n+1)/2
    sol = []
    for a in range(1,n+1):
        b = (total-a)/(a+1.0)
        if b.is_integer() and b <= n:
            sol.append((a,int(b)))
    return sol
'''

def removNb(n):
    # your code
    sum_n = sum(range(1, n+1))
    n_list = list(range(1,n+1))
    real_list = []
    '''
    for i in n_list:
        first = sum_n // i
        if first in n_list:
            real_list.append(i)
    '''
    comp_list = []
    real_list = n_list[(len(n_list)//2) : (len(n_list)-len(n_list)//4)]
    ret_list = []
    for i in real_list:
        second = (sum_n - i) / (i+1)
        string_second = str(second)
        if second in comp_list:
            continue
        if string_second.endswith('.0') and second in n_list:
            comp_list.append(i)
            comp_list.append(int(second))
            ret_list.append((i, int(second)))
            ret_list.append((int(second), i))
    return sorted(ret_list)