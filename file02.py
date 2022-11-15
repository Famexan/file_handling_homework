def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    ans = []

    for i in data.split('\n'):
        ans.append(i)

    return len(ans)

dat = open('./txt_file/data02.txt').read()
print(main(dat))
