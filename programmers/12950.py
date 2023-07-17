def solution(arr1, arr2):
    result = []
    for idx in range(len(arr1)):
        check_arr = []
        for j in range(len(arr1[idx])):
            check_arr.append(arr1[idx][j] + arr2[idx][j])      

        result.append(check_arr)

    return result