import os.path
(1)  os.path.abspath(path) - returns absolute path.
      >>> import os
      >>> os.path.abspath(fnm)
        'E:\\movie\\young sheldon'
(2) os.path.basename(path) - Return the base name of pathname path.
      >>> print fnm
      E:\movie\young sheldon
      >>> os.path.basename(fnm)
      'young sheldon'
(3) os.path.commonprefix(list) - Return the longest path prefix (taken character-by-character) that is a prefix of all
 paths in list. If list is empty, return the empty string (''). 

(4) os.path.dirname(path) - Return the directory name of pathname path. This is the first element of the pair returned by passing path to the
  function split().
      >>> os.path.dirname(fnm)
         'E:\\movie'
(5) os.path.exists(path) - Return True if path refers to an existing path.
      >>. os.path.exists(lst[0])
      False
(6) os.path.expandvars(path) - Return the argument with environment variables expanded.
Substrings of the form $name or ${name} are replaced by the value of environment variable name.

(7) os.path.getatime(path) - Return the time of last access of path.
The return value is a number giving the number of seconds since the epoch (see the time module). 
Raise os.error if the file does not exist or is inaccessible.

(8) os.path.getmtime(path) - Return the time of last modification of path.
The return value is a number giving the number of seconds since the epoch (see the time module).
Raise os.error if the file does not exist or is inaccessible.

(9) os.path.getctime(path) - Return the system’s ctime which

       >>> os.path.getatime(fnm)
      1517665080.986582
      >>> os.path.getmtime(fnm)
      1517665080.986582
      >>> os.path.getctime(fnm)
      1506752348.2193737
(10) os.path.getsize(path) - Return the size, in bytes, of path.
    Raise os.error if the file does not exist or is inaccessible.

     >>> os.path.getsize(fnm)
        4096L
(11) os.path.isabs(path) - Return True if path is an absolute pathname. 
On Unix, that means it begins with a slash, on Windows that it begins with a (back)slash after chopping off a potential
drive letter.

(12) os.path.isfile(path) - Return True if path is an existing regular file. 

(13) os.path.isdir(path) - Return True if path is an existing directory.

(14) os.path.islink(path) - Return True if path refers to a directory entry that is a symbolic link.

          >>> os.path.isabs(fnm)
          True
          >>> os.path.isdir(fnm)
          True
          >>> os.path.islink(fnm)
          False
          >>> os.path.ismount(fnm)
          False
(15) os.path.normcase(path) - Normalize the case of a pathname.
On Windows, it also converts forward slashes to backward slashes.

(16) os.path.normpath(path) - Normalize a pathname by collapsing redundant separators and
up-level references so that A//B, A/B/, A/./B and A/foo/../B all become A/B. 
On Windows, it converts forward slashes to backward slashes.

(17) os.path.realpath(path) - Return the canonical path of the specified filename, 
eliminating any symbolic links encountered in the path.

          >>> os.path.normcase(fnm)
          'e:\\movie\\young sheldon'
          >>> os.path.normpath(fnm)
          'E:\\movie\\young sheldon'
          >>> os.path.realpath(fnm)
          'E:\\movie\\young sheldon'
          >>> fnm = "A:\..\demo\a.py"
          >>> os.path.normpath(fnm)
          'A:\\demo\x07.py'

(18) os.path.samefile(path1, path2) - Return True if both pathname arguments refer to the same file or directory. Not supported on win.
          >>> fnm1 = "E:\movie\config.txt"
          >>> fnm2 = "E:\pyprograms\config.txt"
          >>> import os
          >>> os.path.samefile(fnm1,fnm2)
          Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
          AttributeError: 'module' object has no attribute 'samefile'

(19)os.path.split(path) -  Split the pathname path into a pair, (head, tail) where tail is the last pathname component and 
head is everything leading up to that. 
The tail part will never contain a slash; if path ends in a slash, tail will be empty. 
If there is no slash in path, head will be empty. 
If path is empty, both head and tail are empty. 
Trailing slashes are stripped from head unless it is the root (one or more slashes only).

          >>> fnm1 = ""
          >>> fnm2 = "config.txt"
          >>> fnm3 = "e:\pyprograms\config.txt"
          >>> fnm4 = "e:\pyprograms\\"
          >>> os.path.split(fnm1)
          ('', '')
          >>> os.path.split(fnm2)
          ('', 'config.txt')
          >>> os.path.split(fnm3)
          ('e:\\pyprograms', 'config.txt')
          >>> os.path.split(fnm4)
          ('e:\\pyprograms', '')
          
(20) os.path.splitext(path)
    Split the pathname path into a pair (root, ext) such that root + ext == path, 
    and ext is empty or begins with a period and contains at most one period. 
    Leading periods on the basename are ignored; splitext('.cshrc') returns ('.cshrc', '').
        >>> os.path.splitext(fnm2)
        ('config', '.txt')
        >>> os.path.splitext(fnm1)
        ('', '')
        >>> os.path.splitext(fnm3)
        ('e:\\pyprograms\\config', '.txt')
        >>> os.path.splitext(fnm4)
        ('e:\\pyprograms\\', '')
        
  (21) os.path.walk(path, visit, arg):
  Traverse directory.
      Dir = 'E:\pyprograms\'
      for dirName, subdirList, fileList in os.walk(Dir):
          print('Found directory: %s' % dirName)
          for fname in fileList:
              print('\t%s' % fname)
  
  
  
  
  
  
  
  
  
  
  
  
