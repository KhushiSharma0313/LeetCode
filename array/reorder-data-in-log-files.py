class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def hasNumber(input):
            return any(char.isdigit() for char in input)

        digit_log = []
        letter_log = []

        for i, log in enumerate(logs):
            vals = log.split(" ")
            if hasNumber(vals[1:]): #digit log 
                digit_log.append(log)
            else:
                letter_log.append([' '.join(vals[1:]), vals[0], i])
        res = []

        for log in sorted(letter_log):
            res.append(logs[log[2]])
        
        return res + digit_log
        #split letter and digit 
        # if digit, add to digit log, don't do anything else
        #if letter log, process
        # ddvivide them in key and value pairs in a tuple 
        # then sort them first based on the value, then based on key
        #then join them together both key and value in the letter log 
        #then join letter and digit together and return 




        
        #array of logs 
        #space delimited words 
        # 1st word - identifier 
        #letter logs - words except identifier, lowercase
        #digit logs - words except identifier, digits 
        # reorder
        # letter logs > digit logs 
        # letter logs alphabetically, if content is same sort lexi by their identifier
        # digit logs relative order 
        #return final order 

        #split the logs into words, then it they're letter logs compare each word by other word


        