Regular expresssion uses state machines(DFA/NFA) for pattern matching.
import re
(!) match performs pattern matching at begining:
    >>> re.match('h','hello')
    <_sre.SRE_Match object at 0x021261A8>
    >>> x = re.match('h','hello')
    >>> x.start()
    0
    >>> x.end()
    1
    >>> x = re.match('hi','hellohiee')
    >>> x.start()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'NoneType' object has no attribute 'start'
    
    (2) search() - check occurence inbetween
        >>> x = re.search('h','ellohiee')
        >>> x
        <_sre.SRE_Match object at 0x02126218>
        >>> x.start(), x.end()
        (4, 5)
        
    (3)findall - find all occurence
    
    (4)Replace a pattern by a repacestring in original string
        sub(pattern, replc, string, count = 0, flag = 0) and subn()
        >>> import re
        >>> re.sub("hi", "bye" , "hellohigoawayhihello", 1)
        'hellobyegoawayhihello'      #output is replacement string and number of occurences replaced
        >>> re.sub("hi", "bye" , "hellohigoawayhihello", 2)
        'hellobyegoawaybyehello'    #output is replacement string and number of occurences replaced
        >>> re.sub("hi", "bye" , "hellohigoawayhihello", 3)
        'hellobyegoawaybyehello'    #output is replacement string
        
        >>> re.subn("hi", "bye" , "hellohigoawayHIhello", 2)
        ('hellobyegoawayHIhello', 1)    #output is replacement string and number of occurences replaced
        >>> re.subn("hi", "bye" , "hellohigoawayhihello", 2)
        ('hellobyegoawaybyehello', 2)   #output is replacement string and number of occurences replaced
        
     (5)Special characters:
        (a).            unified search
            >>> x = re.search("a.b","acb")
            >>> x.start()
            0
            >>> x.end()
            3
            >>> x = re.search("a.b","ab")
            >>> print x
            None

        (b)^                match begining but if before [] then it is negation
         >>> x = re.search("^S","Supriya")
        >>> x.start()
        0
        >>> x.end()
        1
        >>> x = re.search("^Sup","Supriya")
        >>> x.end()
        3
        >>> x.start()
        0
        
        (c)$                    end
        >>> x = re.search("ya$","Supriya")
        >>> x.start()
        5
        >>> x.end()
        7
        
        (d)*                    zero or more occurence
            +                   one or more occurence
        >>> x = re.search("a*b*","aaab")
        >>> x.start(), x.end()
        (0, 4)
        >>> x = re.search("a*b*","aabaabaaab")
        >>> x.start(), x.end()
        (0, 3)
        
        (e)?            commit to first possible solution
        >>> x = re.search("a*b*?","aaab")
        >>> x.start(), x.end()
        (0, 3)
        >>> x = re.search("a*b*","aaabbbb")
        >>> x.start(), x.end()
        (0, 7)
        >>> x = re.search("a*b*?","aaabbbb")
        >>> x.start(), x.end()
        (0, 3)    
        >>> x = re.search("a+b+?","aaab")
        >>> x.start(), x.end()
        (0, 4)
        >>> x = re.search("a+b+?","aaabbbb")
        >>> x.start(), x.end()
        (0, 4)
        
        >>> x = re.search("(a*b*)","aaabbbb")
        >>> x.start(), x.end()
        (0, 7)
        >>> x = re.search("(a*b*)?","aaabbbb")
        >>> x.start(), x.end()
        (0, 7)
        >>> x = re.search("(a*b*)","aaabbbba")
        >>> x.start(), x.end()
        (0, 7)
        >>> x = re.search("(a*b*)?","aaabbbba")
        >>> x.start(), x.end()
        (0, 7)
         >>> x = re.search("ab*", "aabbabbb")
        >>> x.start(), x.end()
        (0, 1)
        >>> x = re.search("(ab)*", "abababab")
        >>> x.start(), x.end()
        (0, 8)
        >>> x = re.search("(ab)*", "ababbbab")
        >>> x.start(), x.end()
        (0, 4)
        >>> x = re.search("ab+", "aabbabbb")
        >>> x.start(), x.end()
        (1, 4)
        
        (f) {}                       search range
        >>> import re
        >>> x = re.search("a{1,3}", "aaaa")
        >>> x.start(), x.end()
        (0, 3)
        >>> x = re.search("ab{1,3}", "aaaabbbbb")
        >>> x.start(), x.end()
        (3, 7)
         >>> x = re.search("ab{1,3}?", "aaabbbbbbbbbbbbbbbbb")
        >>> x.start(), x.end()
        (2, 4)
        >>> x = re.search("ab{1,3}", "aaabbbbbbbbbbbbbbbbb")
        >>> x.start(), x.end()
        (2, 6)
        >>> x = re.search("[a-z]+","abczbefg")
        >>> x.start(), x.end()
        (0, 8)
        >>> x = re.search("[a-z]+","abcz1234befg")
        >>> x.start(), x.end()
        (0, 4)
        >>> x = re.search("[a-zA-Z0-9]+","abczbes534$534DFD343fg")
        >>> x.start(), x.end()
        (0, 10)
        
    (6) re.compile(expren) - Compile a regular expression pattern into a regular expression object, which can be used for matching
        re.findall(pattern,string,flag) - Return all non-overlapping matches of pattern in string, as a list of strings. The string is                 
                   scanned left-to-right, and matches are returned in the order found. If one or more groups are present in the pattern,             
                   return a list of groups; this will be a list of tuples if the pattern has more than one group. Empty matches are included                         
                   in the result.
        '.'
           (Dot.) In the default mode, this matches any character except a newline.
           If the DOTALL flag has been specified, this matches any character including a newline.
        '^' 
           (Caret.) Matches the start of the string, and in MULTILINE mode also matches immediately after each newline.
           
        >>> x = re.compile("^a")
        >>> x.findall("a for apple\na for ball")
        ['a']
        
        >>> x = re.compile("^a",re.MULTILINE)
        >>> x.findall("a for apple\na for ball")
        ['a', 'a']
        >>> x.findall("a for apple\nA for ball")
        ['a']

        >>> x = re.compile("^a",re.MULTILINE|re.IGNORECASE)
        >>> x.findall("a for apple\nA for ball")
            ['a', 'A']

        >>> x = re.compile("^a",re.DOTALL)
        >>> x.findall("a for apple\nA for ball")
            ['a']
    
        >>> x = re.compile(".+")
        >>> x.findall("a for apple\nA for ball\na for america")
            ['a for apple', 'A for ball', 'a for america']
    
        >>> x = re.compile(".+",re.DOTALL)
        >>> x.findall("a for apple\nA for ball\na for america")
            ['a for apple\nA for ball\na for america']

        >>> s = "hsdfhsdhf1552s2153154asfdsvh45455"
        >>> x = re.compile("[0-9]+")
        >>> x.findall(s)
            ['1552', '2153154', '45455']
    
    ##Special characters after \ specify some special meaning like \A, \Z, \b, \B, \number, \d, \D, \s, \S, \w, \W
    
        >>> x = re.search("\Aa","aasbfha") #\A Matches only at the start of the string.
        >>> print x.start(),x.end()
            0 1
    
        >>> x = re.search("a\Z","aasbfha") #\Z matches only the end of the string
        >>> print x.start(),x.end()
            6 7

        -> By putting ^ this in start, will invert condition.
            >>> x = re.compile("[^[0-9]+")
            >>> s = "hsdfhsdhf1552s2153154asfdsvh45455"
            >>> x.findall(s)
                ['hsdfhsdhf', 's', 'asfdsvh']

        -> To identify only digits use \d
            >>> x = re.compile("[\d]+")
            >>> x.findall(s)
                ['1552', '2153154', '45455']
            >>> x = re.compile("[\D]+")
            >>> x.findall(s)
                ['hsdfhsdhf', 's', 'asfdsvh']
            >>> 

        -> Match pattern at start of word in sentence.
            \b Matches the empty string, but only at the beginning or end of a word
            >>> x = re.compile(r"\ba\w+")
            >>> s = "apple is awesome,america ris ruled by trump"
            >>> x.findall(s)
                ['apple', 'awesome', 'america']
            >>> 
    
        ->All words starts and ends with "a"
            >>> x = re.compile(r"\ba\w+a\b")
            >>> x.findall(s)
                ['america']
            >>> 

        -> Word not starting with "a"
            >>> x = re.compile(r"\Ba\w*")
            >>> s = "apple is awesome,america rais rulaed by traump"
            >>> x.findall(s)
                ['a', 'ais', 'aed', 'aump']
            >>> x = re.compile(r"\Bm\w*")
            >>> x.findall(s)
                ['me', 'merica', 'mp']
            >>> x = re.compile(r"\w+\Bm\w*")
            >>> x.findall(s)
                ['awesome', 'america', 'traump']
