# Problem statement - https://leetcode.com/problems/maximum-subarray

def max_subarray(arr):
    res_arr = [0 for _ in range(0, len(arr))]
    res_arr[0] = (arr[0], 0) # (max_val, start_idx) format
    #arr[0] = (arr[0],0)  
    for idx in range(1, len(arr)):
        if arr[idx] > (arr[idx] + res_arr[idx-1][0]):
            res_arr[idx] = (arr[idx], idx)
        else:
            res_arr[idx] = (arr[idx] + res_arr[idx-1][0], res_arr[idx-1][1])

    # max_tuple = max(arr, key = lambda x:x[0])
    print(arr)
    print('===')
    print(res_arr)
    start_idx = end_idx = 0
    max_so_far = res_arr[0][0]
    for idx in range(1, len(res_arr)): 
        if res_arr[idx][0] > max_so_far:
            max_so_far = res_arr[idx][0]
            start_idx = res_arr[idx][1]
            end_idx = idx

    max_subarr = arr[start_idx:end_idx+1]
    return max_subarr



if __name__ == "__main__":

    test1 = [-2,1,-3,4,-1,2,1,-5,4]

    print(max_subarray(test1))