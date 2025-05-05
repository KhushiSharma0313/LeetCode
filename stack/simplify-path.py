class Solution:
    def simplifyPath(self, path: str) -> str:
        # time = O(n)
        # memory = O(n) for stack 
        #absolute path - begins with / 
        # abssolute path to simplified canonical path 
        # '.' is current dir, '..' prev or parent, consecuitve slashes are same as single one 
        # if they don't match these rules, treat as valid direc or file 
        # canonical path -> start with /, directories separated by slash, not end with / unless root
        # not have '.' or '..' to represent current or parent 
        # '...' as a file name 
        # retrun canonical path 

        # example /home/ -> /home , /home//foo/ - /home/foo
        # /home/use/documents/../pic -> 

        #/abc/.. means because of double dot, we want to go outside of abc, meaning pop abc 
        # when encounter .., don't include it and pop out direcotry before that
        # single dot '.' is just ignored , remove dot 
        # if no prev directory before .. and just / , then remove .. nothing else 
        # if multiple slashes pop that 

        # we are using stack, because of double dot operator 
        # whenever double dot that's basically pop function 

        #store only the file names 
        stack = []
        # string in between the slashes 
        curr = ""

        #iterate through path 
        for c in path + "/":
            # if it's slash, make decision based on string so far
            if c == "/":
                #if its .. treat it as pop 
                if curr == "..":
                    
                    if stack: stack.pop()
                
                # if it's anything but a empty string or . then append 
                elif curr != "" and curr !=".":
                    stack.append(curr)
                curr = ""
            
            # if it's any other element, add it to string 
            else:
                curr +=c 

        # since at this moment stack only contains files, we need to add slashes to it and start with slash
        return "/" + "/".join(stack)



        