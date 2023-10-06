
run_mini:
	make clean
	fontforge -lang=py -script ./makesvg.py ./example_MINI.json

run_init:
	make clean
	fontforge -lang=py -script ./makesvg.py ./example_INIT.json

run_mine:
	make clean
	fontforge -lang=py -script ./makesvg.py ./example_MINE.json

clean:
	rm -rf ./exp
	mkdir ./exp

show:
	font-manager  output/example.ttf

reverse:
	rm ./output/z.png
	convert -background none -fill black -font ./output/example.ttf -pointsize 300 label:"Z" ./output/z.png
