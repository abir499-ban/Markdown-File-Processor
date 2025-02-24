import re

class mdParser:
    def __init__(self):
        self.rules=[
            (r'^#{1,6}', self.__parse_header),
            (r'\*\*.*\*\*' , self.__parse_boldText),
            (r'\*.*\*' , self.__parse_italicText),
            (r'\>.*' , self.__parse_blockquote),
            (r'^-+$' , self.__parse_hr)
        ]

        pass

    def main(self, text):
        for line in text.splitlines():
            self.checkLine(line)
        pass


    def checkLine(self, line):
        n = len(line)
        i = 0
        while i < len(self.rules):
            match = re.search(self.rules[i][0], line)
            if match:
                print(self.rules[i][1](match , line))
                break
            elif i < len(self.rules) - 1:
                # print('No match going for next')
                i += 1
            else:
                print(f"<p>{line}</p>")
                break
                
        pass


    def __parse_header(self, match , text):
        offset = match.end()
        return f"<h{len(match.group())}>{text[offset:]} </h{len(match.group())}>"
    
    def __parse_boldText(self, match , text):
        string = match.group()
        l = len(string)
        return f"<b>{string[2:l-2]}</b>"

    def __parse_italicText(self, match, text):
        string  = match.group()
        l = len(string)
        return f"<i>{string[1:l-1]}</i>"

    def __parse_blockquote(self, match , text):
        string  = match.group()
        l = len(string)
        return f"<blockquote><p>{string[1:l]}</p></blockquote>"
    
    def __parse_hr(self, match , text):
        return "<hr>"

pass

obj = mdParser()
##obj.main('## this is a header')
##obj.main('*read carefully *')
# obj.main("""# Guide on how to set up the repo.
# **You must have node package manager installed**.
# * version should be more that 6.1.7*
# ---------------
# Run this command
# >npm i express""")





