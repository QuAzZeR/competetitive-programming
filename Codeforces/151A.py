n, k, l, c, d, p, nl, np = [int(i) for i in input().split(' ')]
drink = k*l/nl
limes = c*d
salt = p/np
print (int(min([drink, limes, salt])/n))
