SUBDIRS = cibi ppo

.PHONY: all $(SUBDIRS)

all: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@

upload:
	pip install webdavclient3
	python up.py

download:
	pip install webdavclient3
	python down.py