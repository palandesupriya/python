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
        
        
        
