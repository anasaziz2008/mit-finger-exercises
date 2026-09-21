def sum_str_lengths(L):
    """
    L is a non-empty list containing either: 
    * string elements or 
    * a non-empty sublist of string elements
    Returns the sum of the length of all strings in L and 
    lengths of strings in the sublists of L. If L contains an 
    element that is not a string or a list, or L's sublists 
    contain an element that is not a string, raise a ValueError.
    """
    # Your code here  
    count = 0
    for item in L:
        
        if type(item) is list:
            for sub_string in item:
                if(type(sub_string) is not str):
                    raise ValueError("list contains integers")
                count += len(sub_string)
        elif type(item) is str:
            count += len(item)
        else: 
            raise ValueError("list contains integers")
    return count

# Examples:
print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
# print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
# print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError