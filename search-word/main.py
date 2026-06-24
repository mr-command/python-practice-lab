def exist( sourses : list[list[str]], word):
    result = ''
    for strList in sourses:
        for string in strList:
            if string in word:
                print(f"found {string}")
                result += string
                if len(result) == len(word):
                    break
            print(f"not found {string}")


    if len(result) == len(word):
        return True , result
    
    else:
        return False , result



print(exist([["C","B"],["A","D","A"]], "AMIN"))
