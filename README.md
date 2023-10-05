# png2ttf

## instructions 

Will follow, but the idea is this:

 1. Use the aseprite template to design your own font in a pixel editor (export to `.aseprite` or to `.png` file).
 2. Run the script on your file.
   - Like this `python3 png2ttf.py in_file.png` or
   - like this `python3 png2ttf.py in_file.svg`.
 3. Receive a `.ttf` font as output.

## todo

 - basics.
   - [X] chop png automatically.
   - [X] create svgs automatically.
   - [ ] create ttf automatically.
   - [ ] add python REQUIREMENTS file.

 - polish.
   - [ ] implement the whole thing for windows environments too.
   - [ ] deal with sub repo that converts png to svg (find essential code and replace. or integrate into this project).
   - [ ] modular tests in python, eg with cucumber or similar.
   - [ ] automatically export aseprite to png using python: eg with https://github.com/Eiyeron/py_aseprite

## credits and license

 - credits
  - uses a python script by Javier Rodriguez which can be found here: https://github.com/IngJavierR/PngToSvg
  - uses the font-forge project: https://fontforge.org/docs/tutorial/scripting-tutorial.html
  - some temporary workaround code by me.

 - license
  - font-forge: https://github.com/fontforge/fontforge/blob/master/LICENSE
  - python PIL: https://github.com/python-pillow/Pillow/blob/main/LICENSE
  - my wrapper code: do what you want

## resources

 - interesting
   - https://github.com/benob/png_font_to_ttf
   - https://github.com/Eiyeron/py_aseprite
   - https://github.com/aseprite/aseprite/blob/main/docs/ase-file-specs.md
   - https://fontforge.org/docs/tutorial/scripting-tutorial.html

 - misc
   - https://stackoverflow.com/questions/13278707/how-can-i-convert-svg-files-to-a-font
   - https://stackoverflow.com/questions/12336401/creating-icon-fonts-with-vector-software-i-e-inkscape-and-fontforge
   - https://web.archive.org/web/20170107170808/http://stackoverflow.com/questions/13882328/tools-to-convert-svg-to-ttf
   - https://superuser.com/questions/48879/how-can-i-make-a-font-using-a-png-image
   - https://stackoverflow.com/questions/63380545/how-to-convert-a-set-of-images-into-a-font-ttf-file-with-python
   - https://github.com/pteromys/svgs2ttf/blob/master/svgs2ttf
   - https://stackoverflow.com/questions/63380545/how-to-convert-a-set-of-images-into-a-font-ttf-file-with-python
   - https://github.com/benob/png_font_to_ttf
   - https://github.com/sl2/TTF-to-PNG
   - https://superuser.com/questions/1337567/how-do-i-convert-a-ttf-into-individual-png-character-images

