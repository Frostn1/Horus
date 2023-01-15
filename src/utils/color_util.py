class ColorUtil:
    @staticmethod
    def prRed(skk, end='\n'): print("\033[91m{}\033[00m".format(skk), end=end)

    @staticmethod
    def prGreen(skk, end='\n'): print("\033[92m{}\033[00m".format(skk), end=end)

    @staticmethod
    def prYellow(skk, end='\n'): print("\033[93m{}\033[00m".format(skk), end=end)

    @staticmethod
    def prLightPurple(skk, end='\n'): print("\033[94m{}\033[00m".format(skk), end=end)

    @staticmethod
    def prPurple(skk, end='\n'): print("\033[95m{}\033[00m".format(skk), end=end)

    @staticmethod
    def prCyan(skk, end='\n'): print("\033[96m{}\033[00m".format(skk), end=end)

    @staticmethod
    def prLightGray(skk, end='\n'): print("\033[97m{}\033[00m".format(skk), end=end)

    @staticmethod
    def prBlack(skk, end='\n'): print("\033[98m{}\033[00m".format(skk), end=end)
