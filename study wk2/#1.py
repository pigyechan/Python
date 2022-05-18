def search_name(s_no, s_name, find_no):
        n = len(s_no)
        for i in range(0, n):
            if find_no == s_no:
                return s_name[i]
            else: return "?"
