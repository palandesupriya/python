#create an entire installer/package(collection of multiple python files)
 eg:setup for ROBOT framework
 
 (1)should always have __init__.py and readme.txt file(both can be empty)
 (2)create setup.py file with 
	from distutil.core from setup
	setup(name = "main_folder_name_where_all_files_are",
		version="x.x",
		py_modules=['loose_python_scripts'],
		packages=['folders_With_python_scripts'])
(3)tar.gz,dist and manifest is created when setup.py is run.

(4)python setup.py sdist	#sdist mhanje source distribution
	(source code deu shakto kunala pan, tyala tithe compile karav lagel package)
	python setup.py 
	(binary distribution, mhanje kunala pan fakt module use karayche ahet and source code nahi dyaycha)
	
