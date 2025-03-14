class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"

        arr = ["a"]

        while len(arr)<k:
            curr = []
            for char in arr:
                curr.append(chr(96+(ord(char)-95)%26))
            arr.extend(curr)
            curr = []
        return arr[k-1]

        