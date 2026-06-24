def findBestTime(days : list[int]):

    output = ""

    for i in range(len(days)):
        
        if days[0] > days[i]:

            return "there is no way to increas your mony"
    
    else:

        for day in days:

            for index in range(len(days)):

                if day < days[index]:

                    output = f"you can buy at {day} and sell at {days[index]}"

                    print(output)
        
        
        return output
    

findBestTime([1,1,3,2,4,6])