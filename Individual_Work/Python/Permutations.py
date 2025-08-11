
def permutations(nums) :
        if len(nums) == 0:
            return [[]]
        
        
        perms = permutations(nums[1:])
        res=[]
        for p in perms:
            for i in range(len(p) + 1):
                aux_copy = p.copy()
                aux_copy.insert(i, nums[0])
                res.append(aux_copy)
        return res

#test case
nums = [1,2,3]
print(permutations(nums))
