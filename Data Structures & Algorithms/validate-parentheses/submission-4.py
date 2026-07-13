class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        for i in range(len(s)):
            if s[i] in ["[", "{", "("]:
                seen.append(s[i])

            elif seen:
                if (seen[-1] == "(") and (s[i] == ")"):
                    seen.pop()
                elif (seen[-1] == "[") and (s[i] == "]"):
                    seen.pop()
                elif (seen[-1] == "{") and (s[i] == "}"):
                    seen.pop()
                else:
                    return False
            else:
                return False

        if len(seen) > 0:
            return False
        else:
            return True