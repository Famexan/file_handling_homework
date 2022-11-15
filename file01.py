def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    #data = data.split(',')
    #return list(data)
    ans = []

    for i in data.split(','):
        ans.append(int(i))

    return ans

dat = open('./txt_file/data01.txt').read()
print(main(dat))