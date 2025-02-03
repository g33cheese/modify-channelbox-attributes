# STYLE ***************************************************************************
# content = assignment
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************


def find_caller(self):
    """Find the stack frame of the caller."""
    current_frame = currentframe()

    # On some versions of IronPython, currentframe() returns None if
    # IronPython isn't run with -X:Frames.
    if current_frame:
        current_frame = current_frame.frame_back

    review = "(unknown file)", 0, "(unknown function)"

    while hasattr(current_frame, "f_code"):
        code = current_frame.frame_code
        file_name = os.path.normcase(code.code_filename)
        if file_name == _srcfile:
            current_frame = current_frame.frame_back
            continue

        review = (code.code_filename, current_frame.frame_line_no, code.code_name)
        break

    return review