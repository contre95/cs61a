# Q2: Greatest Pals
# Difficulty: ⭐⭐
# A substring of s is a sequence of consecutive letters within s. Given a string s, greatest_pal should return the longest palindromic substring of s. If there are multiple palindromic substrings of greatest length, then return the leftmost one. You may use is_palindrome.
# IMPORTANT: For this problem, each starter code template is just a suggestion. We recommend that you use the first, but feel free to modify it, try one of the other two or write your own if you'd like to. Comment out the other versions of the function to run doctests.

def is_palindrome(s):
    return s == s[::-1]
def greatest_pal(s):
    """
    >>> greatest_pal("tenet")
    'tenet'
    >>> greatest_pal("tenets")
    'tenet'
    >>> greatest_pal("stennet")
    'tennet'
    >>> greatest_pal("25 racecars")
    'racecar'
    >>> greatest_pal("abc")
    'a'
    >>> greatest_pal("")
    ''
    """
    if is_palindrome(s):
        return s
    left, right = s[:-1], s[1:]
    if is_palindrome(left) or len(left)==2:
        return greatest_pal(left)
    return greatest_pal(right)

# def greatest_pal(s):
    # """
    # >>> greatest_pal("tenet")
    # 'tenet'
    # >>> greatest_pal("tenets")
    # 'tenet'
    # >>> greatest_pal("stennet")
    # 'tennet'
    # >>> greatest_pal("25 racecars")
    # 'racecar'
    # >>> greatest_pal("abc")
    # 'a'
    # >>> greatest_pal("")
    # ''
    # """
    # def helper(a, b, c):
        # if __________________________ > ____________________________:
            # return _______________________________________________
        # elif ________________________ > ____________________________:
            # return _______________________________________________
        # elif ________________ and _______________________________
            # ______________________________________________________
        # return ____________________________________________________
    # return helper(1, 0, "")

# def greatest_pal(s):
    # """
    # >>> greatest_pal("tenet")
    # 'tenet'
    # >>> greatest_pal("tenets")
    # 'tenet'
    # >>> greatest_pal("stennet")
    # 'tennet'
    # >>> greatest_pal("25 racecars")
    # 'racecar'
    # >>> greatest_pal("abc")
    # 'a'
    # >>> greatest_pal("")
    # ''
    # """
    # def helper(a, b):
        # if ______________________________________________________:
            # return ______________________________________________________
        # elif ______________________________________________________:
            # return ______________________________________________________
        # return ______________________________________________________
    # return _________________________________________________________________

