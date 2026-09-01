'''
# How to import file in the py file

# Types of way to import

# 1 import :- used to bring/load the entire module/package. syntax-> import module_names

# 2 as :- Used to give shorter name or alternate name to the module or package. we can alias multiple modules. syntax-> import module_name as m

# 3 from:- Used to import a specific member from a module and only the selected member is imported.syntax-> from module_name import member_names

# --------------------------------------------------DUNDER---------------------------------------------------------

# DUNDER variable-> predefine special variable with double underscores at the start and end. created automatically by python.

# Application/used of dunder variable:-

# 1) identifying modules

# 2) track where files are stores

# 3) provide documentation

# 4) controls how module will behave when they are imported

# types of dunder

1 `__name__` :- provide name of the module.
if module is directly exceuted or if that module executed as resulr
when it is excuted direclty it will give `__main__`

2 `__file__`:- give the full file path of the currently being executed

3 `__package__`:- used to display which package the module belong to 

4 `__cached__`:- gives the full path of the bytecode generated for that module

5 `__doc__` :- sotre the doc string of a module,class,function
    -> doc string = triple quote string written at very begininning of a module,class, funtion
    -> for documentation purpoose and to tell the purpose of that code
'''