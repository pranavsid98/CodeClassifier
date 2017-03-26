train = [
    ("""def fib(n):
            if n==1 or n==2 or n==3:
                return 1
            return fib(n-1) + fib(n-2)""",'BaseCaseError'),
    ("""def fib(n):
            if n==1 or n==2:
                return 1
            return fib(n-1) + n-2""",'RecursionError'),
    ("""def fib(n):
            if n==1 or n==2:
                return 2
            return fib(n-1)+fib(n-2)""",'BaseCaseError'),
    ("""def fib(n):
            a,b = 1,1
            for i in range(n):
                a,b = b,a+b
            return a""", 'IterationRangeError'),
    ("""fibarray = [0,1]
        def fib(n):
            if n<len(fibarray):
                return fibarray[n-1]
            else:
                temp_fib = fib(n-1) + fib(n-2)
                fibarray.append(temp_fib)
                return temp_fib""", 'MemoizationError'),
    ("""def fib(n):
            if n==1 or n==2:
                return 1
            return fib(n-1) + fib(n-3)""", 'RecursionError')
]

test = ["""def fibonac(n):
            if n==1 or n==2:
                return 1
            return fib(n-1) + fib(n-5)""",
"""def fib(n):
            one,two = 1,1
            for i in range(n):
                one,two = two,one+two
            return one"""]


from textblob.classifiers import NaiveBayesClassifier as nb
cl = nb(train)
for sample in test:
    print cl.classify(sample)
