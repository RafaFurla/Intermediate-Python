"""________________readme________________"""
# source code for Private Function in Python
# how to use it is given in the docstring portion of the PrivateFunc class
# please report any bug
# first release: April 6, 2021
# latest update release: April 8, 2021
# version: 1.2.21
"""________________readme________________"""

"""    Copyright (C) 2021 Md. Faheem Hossain fmhossain2941@gmail.com"""

"""    Permission is hereby granted, free of charge, to any person obtaining    a copy of this code, to 
deal in the code without restriction, including    without limitation the rights to use, copy, publish,    
distribute, and to     permit persons to whom the Software is furnished to do so, subject to    
the following conditions:

The above copyright notice and this permission notice shall be    included in all copies or substantial 
portions of the Code.

THE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,    EXPRESS OR IMPLIED, INCLUDING BUT NOT 
LIMITED TO THE WARRANTIES OF    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.    
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY     CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT,    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE    
CODE OR THE USE OR OTHER DEALINGS IN THE CODE."""


class PrivateFunc:
    """ >> description: this is a class which one can use to create private functions
     >> public functions: private
     >> how to use:
     # first of all import this private.py file, then create an object of this class. Before private
     functions use the
     'private' method as a decorator

     >> sample code: (sample.py) __________
     from private import PrivateFunc
     privatefunc = PrivateFunc('sample') # enter the current module name
     # or privatefunc = PrivateFunc('sample', error_name = ImportError, error_message = "false import")
     # error_name is the name of the error which is raised when private function is illegally called
     # and error_message is the message which will be shown with the error
     # either enter both error_name and error_message, or none
     @privatefunc.private
     def a():
         return 10
     # now 'a' is a private function"""

    __slots__ = ["_filename", "__error_name", "__error_message"]
    __version__ = '1.2.21'

    _filename: str
    __error_name: type
    __error_message: str

    def __init__(
            self,
            filename,  # name of the file, where the object of PrivateFunc class is created
            error_name="",  # name of the error which will be raised if private function is called
            # illegally
            error_message=""  # message that will be shown with the error name
            # filename is a default parameter, error_name and error_message are non-default parameters
    ):
        self._filename = filename
        try:
            if error_name:
                self.__error_name = error_name
            else:
                self.__error_name = ImportError
        except Exception:
            self.__error_name = ImportError
        self.__error_message = error_message

    def private(self, func):

        """this is the core function of the class"""

        def wrap(*args, **kwargs):

            from sys import argv
            from inspect import stack
            import os.path as path

            if self._filename != argv[0]:
                # if self._filename == sys.argv[0] that means the function wasn't imported, so it should
                # work
                # otherwise the  function is imported and we have to check how it is imported,
                # I mean who is calling it, is it called by a function of its own filename or else

                # caller_file_module is the name of the file of the function which is calling the private
                # function
                caller_file_module = stack()[1].filename
                caller_file_module = path.splitext(path.basename(caller_file_module))[0]

                if self._filename != caller_file_module:
                    # self._filename == caller_file_module that means a native function is calling the
                    # private function,
                    # so it should run
                    # otherwise, it is being called by a foreign function, which should be blocked
                    if not self.__error_message:
                        raise self.__error_name(
                            "cannot import " + func.__name__ + " from " + self._filename
                            + " because it is a private function")
                    else:
                        raise self.__error_name(self.__error_message)
            func(*args, **kwargs)

        return wrap


"""Obs.: 1. The source code has syntax highlighting. In case you find it hard to read, as I wrote it in my 
PC, so I'll also recommend you to use a wider screen. 2. Since SL only allows a single page for a project,
so I had to find a way to combine 3 python files into 1. Let me say a bit about the demo code: the name of 
those 3 files: a) private.py (source code) b) moduleWithPrivateFunction.py (a file with private functions) 
c) file0.py (the file provided by SL; it calls the functions from the 2nd file and tests if they are 
working properly or not). Please copy line 9-48, 53-61 & 81-111 in 3 different files (as recommended above) 
and then read them. """