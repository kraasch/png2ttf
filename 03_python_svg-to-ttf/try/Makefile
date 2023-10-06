
run:
	make clean
	fontforge -lang=py -script ./makesvg.py ./example.json

clean:
	rm -rf ./exp
	mkdir ./exp

reverse:
	convert -background none -fill black -font example.ttf -pointsize 300 label:"Z" z.png
