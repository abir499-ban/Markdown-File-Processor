import re

class mdParser:
    def __init__(self):
        self.rules=[
            (r'^#{1,6}', self.__parse_header),
            (r'\*\*.*\*\*' , self.__parse_boldText)
        ]

        pass

    def main(self, text):
        n =len(text)
        i = 0
        while True:

            match = re.search(self.rules[i][0] , text)
            if match:
                print(self.rules[i][1](match, text))
                break
            else:
                print('No match going for next')
                i += 1


    def __parse_header(self, match , text):
        offset = match.end()
        print("match : " , match.group())
        print("text: ", text[offset :])
        return f"<h{len(match.group())}>{text[offset:]} </h{len(match.group())}>"
    
    def __parse_boldText(self, match , text):
        string = match.group()
        l = len(string)
        return f"<b>{string[2:l-2]}</b>"

pass

obj = mdParser()
##obj.main('## this is a header')
##obj.main('** read carefully **')



