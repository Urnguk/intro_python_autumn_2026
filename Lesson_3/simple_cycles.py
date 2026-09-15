# A = []
# for i in range(1, 11):
#     A.append(i)
# # print(A)
# # for i in range(len(A)):
# #     print(A[i])
# print(*A)


A = [3, 7, 8, 2, 0, -4, 1]

# summ = 0
# for i in range(len(A)):
#     summ += A[i]
# print(summ)
#
# mult = 1
# for i in range(len(A)):
#     mult *= A[i]
# print(mult)
#
# max_value = -float('inf')
# for i in range(len(A)):
#     if A[i] > max_value:
#         max_value = A[i]
# print(max_value)
#
# max_i = 0
# for i in range(len(A)):
#     if A[i] > A[max_i]:
#         max_i = i
# print(max_i)
#
# max_1 = -float('inf')
# max_2 = -float('inf')
# for i in range(len(A)):
#     if A[i] > max_1:
#         max_2 = max_1
#         max_1 = A[i]
#     elif A[i] > max_2:
#         max_2 = A[i]
# print(max_2)

for i in range(len(A) // 2):
    A[i], A[len(A)-1-i] = A[len(A)-1-i], A[i]

print(A)




