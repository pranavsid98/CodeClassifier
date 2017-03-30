new_train = [
    ("sum = 0;\n\nfor num in range(1000):\n  if (num % 3 == 0) || (num % 5 == 0):\n  \tsum += num\n","Implementation is perfect"),
    ("for num in range(10):\n  a = num % 3\n  b = num % 5\n  c = a + b\n\n\nprint c","Not checking for multiples"),
    ("for num in range(10):\n  if num % 3 == 0 or num % 5 == 0:\n  \tprint num","Prints the multiples, not the sum"),
    ("a = 0\nfor num in range(1000):\n  if num % 7 == 0 or num % 5 == 0:\n\nprint num","Checks for other multiple combinations, not 3 and 5"),
    ("for num in range(1000):\n  \n\tprint x\n  \n  ","Not checking for multiples"),
    ("a=0\nfor num in range(1000):\n  if (num % 3 == 0):\n\ta=a+num\n  else if (num % 5 ==0):\n\ta=a+num\nprint num","Prints the multiples, not the sum"),
    ("suma=0\nfor num in range(100) :\n  if num % 3==0 or num % 5 == 0 : \n    suma = suma + num\n\nsum=0\nfor num in range(1000) :\n  if num % 3==0 or num % 5 == 0 : \n    sum = sum + num\n  \nprint suma*10000+sum","Incorrect sum"),
    ("for num in range(10):\n  print '%'\n  ","Prints random value"),
    ("for num in range(1000):\n  if num % 3 == 0:\n\tsum = sum + num\n\tprint sum\n  elif num % 5 == 0:\n\tsum = sum + num\n\tprint num\n\n\t\n ","Implementation is perfect"),
    ("for num in range(10):\\n  if (num%3 == 0):\\n\\tn=n+num\\n  if (num%5 == 0):\\n\\tn=n+num\\n\\nprint n","Else-if instead of 'if' would work"),
    ("for num in range(10): 'print x'\\n  \\n  \\n  ","Not checking for multiples"),
    ("sum=0\\nfor num in range(1000):\\n  if num%3==0 or num%5==0:\\n\\tsum += num\\n\\t\\nprint(sum)\\n  ","Implementation is perfect"),
    ("total = 0\\nfor num in range(10):\\n  if num % 3 == 0 or num%5 == 0:\\n\\ttotal += num\\nprint total\\n","Incorrect sum"),
    ("for num in range(10):\\n  num % 3\\n  print num","Not checking for multiples"),
    ("for num in range(10):\\n  if (num % 5 == 0):\\n\\tnum = num + num\\n\\t\\n\\t\\nprint num \\n  ","Checks for other multiple combinations, not 3 and 5"),
    ("for num in range(1000):\\n  if(num % 3 == 0)\\n  \\tprint num","Checks for other multiple combinations, not 3 and 5"),
    ("sum = 0;\\nfor num in range(1000):\\n  if (num%3 == 0):\\n\\tsum = sum + 3;\\n  if (num%5 == 0):\\n\\tsum = sum + 5;\\n\\nprint sum;\\n\\n  \\t","Implementation is perfect"),
    ("for num in range(3, 5): print 3\\n \\n  \\n  ","Not checking for multiples"),
    ("sum=0\\nfor num in range(1000):\\n  if num % 3 == 0:\\n\\tsum = sum + num\\n\\tprint sum\\n  elif num % 5 == 0:\\n\\tsum = sum + num\\n\\tprint num\\n\\n\\t\\n ","Incorrect sum"),
    ("for num in range(1000):\\n  if (num % 3) = 0\\n      print num","Checks for other multiple combinations, not 3 and 5"),
    ("sum = 0\\nfor num in range(1000):\\n  if num % 3 == 0 or num % 5 == 0\\n    sum = sum + num\\nprint sum","Implementation is perfect"),
    ("for num in range(1000):\\n  if num % 3 == 0:\\n  print (num)\\n","Checks for other multiple combinations, not 3 and 5"),
    ("total = 0\\nfor num in range(1000):\\n  if (num % 3 == 0) || (num % 5 == 0)\\n  \\ttotal = total + num\\nprint total\\t\\n","Implementation is perfect"),
]

new_test = [
    ("total = 0\\nfor num in range(1000):\\n  if (num % 3 == 0) || (num % 5 == 0)\\n  \\ttotal = total + num\\nprint total\\t\\n","Implementation is perfect"),
    ("for num in range(1000):\\n  if num % 3 == 0:\\n  print (num)\\n","Checks for other multiple combinations, not 3 and 5"),
    ("sum=0\\nfor num in range(1000):\\n  if num % 3 == 0:\\n\\tsum = sum + num\\n\\tprint sum\\n  elif num % 5 == 0:\\n\\tsum = sum + num\\n\\tprint num\\n\\n\\t\\n ","Incorrect sum"),
    ("for num in range(5000000): 'print x'\\n  \\n  \\n  ","Not checking for multiples"),
]






from textblob.classifiers import NaiveBayesClassifier as nb
cl = nb(new_train)
print cl.accuracy(new_test)
test = [x[0] for x in new_test]
for sample in test:
    print cl.classify(sample)
    prob_dist = cl.prob_classify(sample)
    print round(prob_dist.prob(cl.classify(sample)), 2) 







































