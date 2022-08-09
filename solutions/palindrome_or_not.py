
def two_sum(target):
    num_list = [0,1,1,2,2,3,4,5]
    len_num_list = len(num_list)
    for i in range(0, len_num_list-1):
        if num_list[i] + num_list[i+1] == target:
           print("location {0} and {1}".format(i, i+1))
           exit(0)
    print("No matching locations")

#two_sum(19)


#read the array
#If array [i+1] < array[i], set buy
# If array[i+1] > array[i], set sell
def buy_sell(prices):
    prices_len = len(prices) - 1
    for i in range(0, prices_len):
        #print(i)
        if prices[i+1] < prices[i]:
            buy = prices[i+1]
            print(buy)
        else:
            sell = prices[i+1]
            print(sell)
    profit = buy - sell
    print(profit)

#buy_sell([7,1,5,3,6,4])

def product_array(nums):
    sum = 1
    for i in nums:
        sum = sum * i
    print(sum)
    for j in nums:
        print(sum//j)


product_array([1,2,3,4])

