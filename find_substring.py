# def solution(a,b):
#     A = str(a)
#     B = str(b)
#     C = B.find(A)
#     return C

def solution(A,B):
  A = str(A)
  B = str(B)

  out = []
  for pos in range(len(B)):
      if(A == B[pos:pos+2]):
        out.append(pos)
  return out
Result = solution(53,1932536753)
print(Result)



# a=53
# b=196853877
# print(solution(a,b))