from typing import List, Tuple

def histogram(input_dictionary: dict) -> list:
    # data is a dictionary that contains the following keys: 'data', 'n', 'min_val', 'max_val'
    # n is an integer
    # min_val and max_val are floats
    # data is a list

    # Write your code here
    data = []
    data = input_dictionary['data'][:]
    min_val = input_dictionary['min_val']
    max_val = input_dictionary['max_val']
    num = input_dictionary['n']

    if(min_val == max_val): #2
        print("Error: min_val and max_val are the same value")
        return []
    if( num < 0): #3
        return []
    if(min_val > max_val): #4
        temp = min_val
        min_val = max_val
        max_val = temp
    if(num == 0):#5
        return []
    hist = num * [0] #6

    w = (max_val - min_val)/num #7

    range_lower = min_val
    range_upper = min_val + w
    i_value = 0
    loop_var = 0

    for number in data:
        if((number < max_val) & (number > min_val)):
            while (loop_var == 0):
                if((number >= range_lower) & (number < range_upper)):
                    hist[i_value] +=1
                    i_value = 0
                    loop_var = 1
                    range_lower = min_val
                    range_upper = min_val + w
                else:
                    i_value += 1
                    range_lower += w
                    range_upper += w
            loop_var = 0
    

    return hist
    # return the variable storing the histogram
    # Output should be a list
    pass

# Here, the function first checks if the lower and upper bounds are the same, 
# if they are it prints an error message and returns an empty list. 
# If lower bound is greater than upper bound, it swaps their values. 
# If number of bins is less than or equal to 0, it returns an empty list. 
# Then it initializes an empty list hist of length n and calculates the width of each bin. 
# Then it iterates through the data, 
# and for each value checks if it is within the range of the histogram and if it is, 
# it increments the bin it belongs to. Finally, it returns the histogram.

def combine_birthday_data(person_to_day: List[Tuple[str, int]], 
                          person_to_month: List[Tuple[str, int]], 
                          person_to_year: List[Tuple[str, int]]) -> dict:
    #person_to_day, person_to_month, person_to_year are list of tuples

    # Write your code here
    month_to_people_data = {}
    num_month = 12 * [0]
    num = 0
    num_total = 0
    loopvar =0
    index = 1
    index2 = 0

    for month in person_to_month:
        num = month[1]
        num_month[num - 1] += 1
        num_total += 1
        #print("occurance = {}, month = {}".format(num_month[num -1], num))

    for month in num_month:
        #print(month)
        if(month == 1):
            month_to_people_data[index] = ()
            while loopvar < num_total:
                if(person_to_month[loopvar][1] == index):
                    month_to_people_data[index] = (person_to_month[loopvar][0], person_to_day[loopvar][1], person_to_year[loopvar][1], 2025 - person_to_year[loopvar][1])
                    #print(month_to_people_data[index])
                loopvar += 1
            loopvar = 0
        elif (month > 1):
            month_to_people_data[index] = month * [1]
            while loopvar < num_total:
                if(person_to_month[loopvar][1] == index):
                    month_to_people_data[index][index2] = (person_to_month[loopvar][0], person_to_day[loopvar][1], person_to_year[loopvar][1], 2025 - person_to_year[loopvar][1])
                    #print(month_to_people_data[index])
                    index2 +=1
                loopvar += 1
            loopvar = 0
        index += 1
        index2 = 0

    # return the variable storing output
    # Output should be a dictionary
    return month_to_people_data

    pass

# We first define the current year as 2024, which will be used to calculate the age of each person later on.
# We create an empty dictionary month_to_people_data that will store the final data in the format specified in the problem statement.
# We iterate over the both values in the tuple of the person_to_month list (note that person_to_month is a list of tuples, which means each item in the list is a tuple) 
# using a for loop. For each iteration, we extract the corresponding day, year and age values from the person_to_day and person_to_year lists using the current name as the "key".
# We then use the current month as the key and a tuple of (name, day, year, age) as the value to update the month_to_people_data dictionary.
# Only change the value to a list data type, when there are multiple entries with the same key. This will help append for other tuples to the same month.
# Finally, we return the month_to_people_data dictionary as the output of the function.
