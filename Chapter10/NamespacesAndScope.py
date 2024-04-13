'''Consider a variable width that’s in the module make_window.py. In which of the
following contexts is width in scope?'''


#within the module itself
#in global or local scope of this module file

#(B) inside the resize() function in the module
#yes

#(C) within the script that imported the make_window.py module
#No
#width is in the namespace of the make_window module, not in the namespace of the importing script.