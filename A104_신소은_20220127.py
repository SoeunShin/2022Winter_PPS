# LeetCode 804 - Unique Morse Code Words

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        codeArr = []
        for i in range(len(words)):
            code = ''
            for j in range(len(words[i])):
                code += morse[ord(words[i][j])-97]
            codeArr.append(code)

        return len(set(codeArr))