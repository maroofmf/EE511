__author__ = 'maroof'



fileName = 'NJGAS.dat'
file= open(fileName,'r')
fileData = file.readlines(),



 ''' Performing coin flip and counting number of heads'''
# for exp_no in range(0,no_experiments):
#     for tosses in range(0,no_coin_tosses):
#         outcome = bernoulli.rvs(0.5,size=1)   # 1 for heads
#         if outcome == 1:
#             no_heads += 1
#     heads.append(no_heads)
#     tails.append(13-no_heads)
#     no_heads = 0