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
    
