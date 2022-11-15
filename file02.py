def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    data = data.split('\n')
    return len(data)
   

dat = open('./txt_file/data02.txt').read()
print(main(dat))
