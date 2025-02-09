import re

class mdParser:
    def __init__(self):
        self.rules=[
            (r'^#{1,6}', self.parse_header)
        ]

        pass

    def main(self, text):
        n =len(text)
        match = re.search(self.rules[0][0] , text)
        if match:
            offset = match.end()
            print("match : " , match.group())
            print("text: ", text[offset :])
            print(self.rules[0][1](match.group() , text[offset:]))
        else:
            print('No macth')


    def parse_header(self, operator, text):
        return f"<h{len(operator)}>{text} </h{len(operator)}>"

pass

# obj = mdParser()

# obj.m("## This is my Name")


