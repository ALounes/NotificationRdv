TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"
CONFIG_FILE := ./config


setup:
	@echo $(TAG)Install prod requirements$(END)
    pipenv install