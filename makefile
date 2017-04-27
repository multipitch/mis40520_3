.PHONY: all
.PHONY: clean

all: data.py kidney.mos
	./data.py
	mosel kidney.mos
	./results.py
clean:
	@rm -f *.csv *.bdg *.bim *.jpg *.gexf *.gephi *.gif 
	@rm -f *.pdf *.png *.svg *.ps *.eps

