a = int(input('Enter the number of rows  '));
n=2*a;
for a in range(1, a+1):
    print(' '*n, end='')
    print('* '*(a))
    n-=1