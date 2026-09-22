class Solution:
    def encode(self, strs: List[str]) -> str:
        header = []

        for s in strs:
            header.append(str(len(s)))
            header.append("-")
        header.append(":")
        header.extend(strs)

        return "".join(header)

    def decode(self, s: str) -> List[str]:
        header = []
        curr_len = []
        i = 0
        answer = []

        # parse header
        while s[i] != ":":
            if ord("0") <= ord(s[i]) <= ord("9"):
                curr_len.append(s[i])
            else:
                header.append(int("".join(curr_len)))
                curr_len = []
            i += 1
        i += 1  # move pointer after ":" in s

        # decode list of strings
        for s_len in header:
            answer.append(s[i : i + s_len])
            i += s_len

        return answer
