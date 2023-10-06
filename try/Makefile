
run_init:
	make clean
	fontforge -lang=py -script ./makesvg.py ./xample_INIT.json

run_mini:
	make clean
	fontforge -lang=py -script ./makesvg.py ./xample_MINI.json

run_mine:
	make clean
	fontforge -lang=py -script ./makesvg.py ./xample_MINE.json

clean:
	rm -rf ./exp
	mkdir ./exp

show:
	font-manager  ./exp/example.ttf

reverse:
	rm ./output/z.png
	convert -background none -fill black -font ./output/example.ttf -pointsize 300 label:"Z" ./output/z.png
