from googlesearch import search

def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1

def google_search( input_statement ): 
    start_ind = find_str(input_statement, 'search ') 
    q = input_statement[start_ind+len('search '):]
    print( q )

    result_statement = """Here are some of links that might help you : 
    """

    for j in search( q, tld="co.in", num=10, stop=10, pause=2):
        result_statement += j + """"
        
        """
    

    return result_statement