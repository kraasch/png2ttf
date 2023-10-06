
run_init:
	make clean
	fontforge -lang=py -script ./makesvg.py ./example_INIT.json

run_mini:
	make clean
	fontforge -lang=py -script ./makesvg.py ./example_MINI.json

run_mine:
	make clean
	fontforge -lang=py -script ./makesvg.py ./example_MINE.json

clean:
	rm -rf ./exp
	mkdir ./exp

reverse:
	convert -background none -fill black -font example.ttf -pointsize 300 label:"Z" z.png
