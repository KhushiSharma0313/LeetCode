class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #make a word from begin word to end word
        # end word needs to be part of word list 
        # constraint - adjacent word differ by single letter 
        # return shortest sequence 
        # every word exact same length 
        # graph problem
        # edges are bidirectional
        # build an adjacency list of the nodes 
        # time complexity = n^2m not acceptable cause n is large so it'll be n*m^2
        # do BFS, which is n^2*m

        #to form adjacency list
        # when we take a word -> think of all patterns we can have by changing one word
        # e.g. -> hot = *ot, h*t, ho*
        # do this with all words, and find out which pattern matches 
        # create a hasmap -> key is the pattern, then values are words that fit this pattern 
        # for this list we're going throgh each word so n, then we're going through it len(n) which is m, and add each word to list is m 
        # so it's O(nm^2)

        #now that we have list and graph, apply bfs to find shortest path
        # go from each node to it's neighbour, and keep counting the path
        # not revisit same neighbour or edge twice 
        # time = total word is m(len of word), then total edge is n^2 = mn^2
        # note for graph with n nodes max edges is n^2
        #count the layers and retrun it 

        if endWord not in wordList:
            return 0
        
       
        #for mapping the pattern from list 
        nei = collections.defaultdict(list)
        wordList.append(beginWord)

        #filling up adjacency list 
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        #data strcuture for bfs 
        visit = set([beginWord])
        q = deque([beginWord])
        

        while q:
            res = 1
            #for each word in the list
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    #check each word matching the pattern
                    for neigword in nei[pattern]:
                        if neigword not in visit:
                            visit.add(neigword)
                            q.append(neigword)

                res +=1
        return 0





        