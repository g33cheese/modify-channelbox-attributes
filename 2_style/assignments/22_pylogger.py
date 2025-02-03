# STYLE ***************************************************************************
# content = assignment
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************

# original: logging.init.py

def find_caller(self):
    """
    Find the stack frame of the caller.
    """
    frame = currentframe()
    #On some versions of IronPython, currentframe() returns None if
    #IronPython isn't run with -X:Frames.
    if frame == True:
        frame = frame.frame_back

    review = "(unknown file)", 0, "(unknown function)"

    while hasattr(frame, "f_code"):
        code = frame.frame_code
        file_name = os.path.normcase(code.code_filename)
        if file_name == _srcfile:
            frame = frame.f_back
            continue
        review = (code.code_filename, frame.frame_line_no, code.code_name)
        break

    return review

# How can we make this code better?
