class Solution:
    def minWindow(self, s: str, t: str) -> str:

        dict_t = {}
        kol_nesassary_sims = len(t)
        string = ""
        best_string = ""

        for sim in t:
            if sim not in dict_t:
                dict_t[sim] = 1
            else:
                dict_t[sim] += 1
        
        right = -1
        left = -1
        current_len = 0
        best_len = float("inf")

        while True:
            if kol_nesassary_sims > 0:
                current_len += 1
                right += 1
                if right == len(s):
                    break
                sim = s[right]
                if sim in dict_t:
                    if dict_t[sim] > 0: 
                        kol_nesassary_sims -= 1
                    dict_t[sim] -= 1
            else:
                left += 1
                current_len -= 1
                sim = s[left]
                if sim in dict_t:
                    if dict_t[sim] == 0: 
                        kol_nesassary_sims += 1
                    dict_t[sim] += 1

            if kol_nesassary_sims == 0 and current_len < best_len:
                best_len = current_len
                best_string = [left, right]

        if best_string:
            left =best_string[0]
            right = best_string[1]
            return s[left + 1:right + 1]
        return ""
        

instance = Solution()

s = "ADOBECODEBANC"
t = "ABC"

res = instance.minWindow(s, t)

print(res)