# (0, 3K)同士にして
# (黒の個数を数えていく -> これが達成できた希望の数. そうすると
# 黒の個数何個,白の個数何個か?
N, K = list(int, input())

black_box = [[0] * 2*K for _ in range(3*K)]
white_box = [[0] * 2*K for _ in range(3*K)]
b_will = 0
w_will = 0
for _ in range(N):
    x, y, c = input().split()
    n = 1 if c == "B" else -1
    if c == "B":
        b_will += 1
        black_box[x % (2*K)][y % (2*K)] += 1
        black_box[x % (2*K) + K][y % (2*K) + K] += 1
    else:
        w_will += 1
        white_box[x % (2*K)][y % K] += 1

sum_b_x_box = [[0] * 2 *K for _ in range(2*K)] # (0, y)-(x,y)までの総和
sum_w_x_box = [[0] * 2 *K for _ in range(2*K)] # (0, y)-(x,y)までの総和
sum_b_y_box = [[0] * 2 * K for _ in range(2*K)] #(x,0)-(x,y)までの総和
sum_w_y_box = [[0] * 2 * K for _ in range(2*K)] #(x,0)-(x,y)までの総和
will_box = [[0] * 2 * K for _ in range(2*K)] 

for i in range(2*K):
    for j in range(2*K):
        if i == 0:
            sum_b_x_box[i][j] = black_box[i][j]
            sum_w_x_box[i][j] = white_box[i][j]
        else:
            sum_b_x_box[i][j] = black_box[i][j] + sum_b_x_box[i-1][j]
            sum_w_x_box[i][j] = white_box[i][j] + sum_w_x_box[i-1][j]

for i in range(2*K):
    for j in range(2*K):
        if j == 0:
            sum_b_y_box[i][j] = black_box[i][j]
            sum_w_y_box[i][j] = white_box[i][j]
        else:
            sum_b_y_box[i][j] = black_box[i][j] + sum_b_y_box[i][j-1]
            sum_w_y_box[i][j] = white_box[i][j] + sum_w_y_box[i][j-1]

b_will_plus = 0
w_will_loss = 0
for i in range(K):
    b_will_plus += sum_b_x_box[i][K-1]
    w_will_loss += sum_w_x_box[i][K-1]
base = b_will_plus + w_will - 2*w_will_loss 
ans = 0


for i in range(2*K):
    for j in range(K):
        if i == 0 and j == 0:
            will_box[0][0] = base
        elif j == 0:
            will_box[i][j] = will_box[i-1][j] - sum_y_box[i][-1] + sum_y_box[(i+K) % (2*K)][-1]
        else:
            if i < K:
                max_box[i][j] = max_box[i][j-1] + (sum_x_box[-1][j-1] - sum_x_box[i+K][j-1]) + sum_x_box[i-1][j-1]-sum_x_box[0][j-1] \
                      - (sum_x_box[i+K-1][j-1] - sum_x_box[i][j-1])
            else:
                max_box[i][j] = max_box[i][j-1] + (sum_x_box[i][j-1]-sum_x_box[(i+K-1)%(2*K)][j-1]) \
                      - (sum_x_box[-1][j-1] - sum_x_box[i-1][j-1] + sum_x_box[(i+K)%(2*K)][j-1] - sum_x_box[0][j-1])
        ans = max(ans, max_box[i][j])
print( )
    