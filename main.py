# Lambda function are for convenience
# Lambda Functions are also called anonymous functions too
# are one liner function which are use to create function without actually creating one

def add(a, b):
    return a + b

print(add(1,2))

minus = lambda x, y: x-y

# the above written line is similar to below given function

def minus(x, y):
    return x - y

print(minus(5, 3))

def a_first(a):
    return a[1]

a = [[1, 14], [5, 6], [8, 23]]
a.sort(key=lambda x:x[1])
print(a)