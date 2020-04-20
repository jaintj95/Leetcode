# Problem Statement - https://leetcode.com/problems/group-anagrams


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""


def groupAnagrams(strs):
    ana_map = {}
    
    for word in strs:
        chars = tuple(sorted(word))

        if chars not in ana_map:
            ana_map[chars] = [word]
            
        else:
            ana_map[chars].append(word)
    
    
    out_list = [0 for _ in range(len(ana_map))]
    
    for idx, keys in enumerate(ana_map.keys()):
        out_list[idx] = ana_map[keys]
        
    return out_list


if __name__ == '__main__':
    result = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result)