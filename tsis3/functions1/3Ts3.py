
def solve(numheads, numlegs):
    #numlegs = 2ch + 4rab
    #numheads = ch + rab
    rab = 0.5 * (numlegs - 2*numheads)
    ch = numheads - rab
    print("колво куриц = "+str(ch)," колво кроликов = "+str(rab))
print("Введите количество ног ")
numlegs = int(input())
print("Введите количество голов ")
numheads = int(input())
solve(numheads,numlegs)

