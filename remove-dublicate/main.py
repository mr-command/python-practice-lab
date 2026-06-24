def removeDuplicates(nums : list[int]):
        output = []
        for i in nums:
            if i not in output:
                output.append(i)
                
                
        return output

print(removeDuplicates([1,1,1,3]))
