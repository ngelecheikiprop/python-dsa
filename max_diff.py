class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        return self.find_max(num) - self.find_min(num)

    def find_max(self, num):
        """to find the max value of a number"""
        num_str = str(num)
        # print(type(num_str))
        for letter in num_str:
            # print(f"letter for now is {letter}")
            if letter != '9':
                # print(f"type of num_str is {type(num_str)}")
                replace_str = num_str.replace(letter, "9")
                # print(f"after replacing {replace_str}")
                break
        return int(replace_str)

    def find_min(self, num):
        """to find the min value of a number"""
        num_str = str(num)
        # print(type(num_str))
        i = len(num_str) - 1
        while i >= 0:
            letter = num_str[i]
            # print(f"letter for now is {letter}")
            if letter != '0':
                # print(f"type of num_str is {type(num_str)}")
                replace_str = num_str.replace(letter, "0")
                # print(f"after replacing {replace_str}")
                break
        return int(replace_str)