#find average of 2 input numbers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    sumOfNumbers = 0
    for x in nums:
        sumOfNumbers = sumOfNumbers + x
        avg = sumOfNumbers / len(nums)    
    fptr.write('%.2f' % avg + '\n')
    fptr.close()
