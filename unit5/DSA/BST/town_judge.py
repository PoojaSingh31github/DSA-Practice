def findJudge(N, M, trust):
  in_degree = [0] * (N + 1)
  out_degree = [0] * (N + 1)
  
  for a, b in trust:
      out_degree[a] += 1  
      in_degree[b] += 1  
  
  # Find the person who satisfies the conditions of the town judge
  for i in range(1, N + 1):
      if in_degree[i] == N - 1 and out_degree[i] == 0:
          return i

  return -1

# Input
N, M = map(int, input().split())  
trust = [list(map(int, input().split())) for _ in range(M)]  

print(findJudge(N, M, trust))
