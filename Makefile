.PHONY: con
# ex: make con dir=abc100
con:
ifndef dir
	$(error dir is undefined)
endif
	mkdir -p $(dir)
	echo '' > $(dir)/a.py
	echo '' > $(dir)/b.py
	echo '' > $(dir)/c.py
	echo '' > $(dir)/d.py
	echo '' > $(dir)/e.py
	echo '' > $(dir)/f.py
