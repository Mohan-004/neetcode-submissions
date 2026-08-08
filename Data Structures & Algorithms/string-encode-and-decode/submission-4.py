class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs :
            return ""
        out_str = ""
        for s in strs :
            if not s :
                out_str += "+--"
            else :
                out_str += s +"--"
        return out_str.strip("--")


    def decode(self, s: str) -> List[str]:
        if not s :
            return []
        out_strs = []
        for i in s.split("--"):
            if i == "+" :
                out_strs.append("")
            else :
                out_strs.append(i)
        return out_strs
