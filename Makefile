all: slides/index.html

DATA_FILES = $(wildcard data/*.R)
DATA_RDA = $(DATA_FILES:R=rda)

data/%.rda:data/%.R
	Rscript -e "source('$<')"

slides/index.html: index.Rmd css/custom.css $(DATA_RDA) theme_soa.R
	Rscript -e "rmarkdown::render('index.Rmd')"
	mkdir -p slides
	mv -f index.html slides/index.html

clean:
	rm -rf data/*.rda
	rm -f slides/index.html
