filename=bare_conf

all:
	pdflatex ${filename}.tex
	bibtex ${filename}.aux
	pdflatex ${filename}.tex
	pdflatex ${filename}.tex
clean : 
	rm -f ${fileName}.aux ${fileName}.bbl ${fileName}.blg ${fileName}.dvi ${fileName}.ps
	rm -f *.log *.bbl *.blg *.aux
	rm -f *.synctex.gz
	rm -f *.pdf
	rm -f fig/*eps-converted-to.pdf
	rm -f image/*eps-converted-to.pdf
	rm -f results/*eps-converted-to.pdf
