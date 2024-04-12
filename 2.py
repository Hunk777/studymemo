def judge(num):
  if num == 87:
    return True
  
  elif num == 3e3:
    return True
 
  else:
    return num % 2 == 0

result1 = judge(87)
result2 = judge(3e3)
result3 = judge(123)
result4 = judge(94)
result5 = judge(4e2)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
#AAA




