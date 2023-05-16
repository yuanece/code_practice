"""
My solution to Mondriaan's Dream Problem
The detailed description of the problem can be found in the link http://poj.org/problem?id=2411
"""

def Mondriaan(width, height):
    """
    input: the length and width of the chessboard
    output: how many cases the chessboard can be completely filled by 1X2 blocks
    0 < width <= 11, 0 < height <= 11;
    """
    N = 2**height
    dp = N*[0]
    dp[-1] = 1

    def transition_exist(b1, b2):
        """
        determine whether the state transition between b1 and b2 is correct.
        b1 is the binary expression for the number n1, b2 is the binary expression for the number n2.
        """
        M = len(b1)
        s = 0
        for m in range(M):
            if b1[m] == '0':
                if b2[m]!= '1':return False
                if s%2 != 0: return False
            else:
                if b2[m] == '0':
                    if s%2!=0:return False
                else:
                    s += 1
        if s%2 == 0:
            return True
        else:
            return False

    map_dict = defaultdict(list)
    for n1 in range(N):
        for n2 in range(N):
            b1 = bin(n1)[2:]
            b2 = bin(n2)[2:]
            b1 = (height-len(b1))*'0'+ b1
            b2 = (height-len(b2))*'0'+ b2
            if transition_exist(b1, b2):
                map_dict[n2].append(n1)


    for iteration in range(width):
        mid = N*[0]
        for n in range(N):
            if n == 0:
                mid[n] = dp[-1]
                continue
            for neighbor in map_dict[n]:
                mid[n] += dp[neighbor]
        dp = mid.copy()
    return dp[-1]
   
if __name__ == "__main__":
    width, height = 4, 11
    case = Mondriaan(width, height)
    print (case)
    # The expected case for 4X11 chessboard is 51205.
    
   



