import torch
print(torch.cuda.is_available())

# string =  "the quick brown fox jumps over the lazy dog"
#
# word1 = "quick"
# word2 = "jumps"
#
# w1_list = []
# w2_list = []
#
# for i, s in enumerate(string):
#
#     if string[i:i+len(word1)] == word1:
#         w1_list.append(i)
#
#     if string[i:i+len(word2)] == word2:
#         w2_list.append(i)

cost = [
    [1, 2, 3],
    [4, 8, 2],
    [1, 5, 3]
]

m = len(cost)
n = len(cost[0])

final_x = m-1
final_y = n-1

def findmincost(x,y):

    if x>=m or y>=n:
        return float('inf')

    if x==m-1 and y==n-1:
        path_cost = cost[x][y]
        return path_cost

    else:
        path_cost = cost[x][y] + min(findmincost(x+1,y),
                                     findmincost(x+1,y+1),
                                     findmincost(x,y+1))

        return path_cost

cost_min = findmincost(0,0)
