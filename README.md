# png2ttf

## instructions 

Will follow, but the idea is this:

 1. Use the aseprite template to design your own font in a pixel editor (export to `.aseprite` or to `.png` file).
 2. Run the script on your file.
   - Like this `python3 png2ttf.py in_file.png` or
   - like this `python3 png2ttf.py in_file.svg`.
 3. Receive a `.ttf` font as output.

## todo

Basics:

 - [X] chop png automatically.
 - [X] create svgs automatically.
 - [ ] create ttf automatically.
 - [ ] add python REQUIREMENTS file.

Polish:

 - [ ] export to otf format too.
 - [ ] implement the whole thing for windows environments too.
 - [ ] deal with sub repo that converts png to svg (find essential code and replace. or integrate into this project).
 - [ ] modular tests in python, eg with cucumber or similar.
 - [ ] automatically export aseprite to png using python: eg with https://github.com/Eiyeron/py_aseprite

## how it works (or will work)

Step one -- from aseprite to PNG:
The user creates a new font using the template and saves it with a transparent background.
After run by the user, `png2ttf` detects if it is run on a `.png` or an `.aseprite` file.
Aseprite files are automatically converted into PNGs.

Step two -- chop chop:
Then `png2ttf` chops the PNG into single file PNGs per glyph.
The template's grid is used as the basis of where to split the PNG.
Each cell in the template is associated with a specific glyph.

Step three -- from PNG to SVG:
Each PNG file containing one glyph then is converted into a respective SVG file.

Step four -- from SVG to TTF:
Each SVG file containing one glyph is compiled into a single TTF file using the FontForge project.
Note: The FontForge project includes a python interpreter.

## credits and license

Credits:

 - The converter is inspired by a script by Javier Rodriguez which can be found here: https://github.com/IngJavierR/PngToSvg
 - Uses the font-forge project: https://fontforge.org/

License:

 - FontForge: Revised BSD License, see [FontForge's license on Github]https://github.com/fontforge/fontforge/blob/master/LICENSE.
 - My wrapper code: do what you want.

## resources

Interesting:
 - https://github.com/benob/png_font_to_ttf
 - https://github.com/Eiyeron/py_aseprite
 - https://github.com/aseprite/aseprite/blob/main/docs/ase-file-specs.md
 - https://fontforge.org/docs/scripting/scripting.html
 - https://fontforge.org/docs/tutorial/scripting-tutorial.html
 - https://fontforge.org/docs/scripting/scripting-alpha.html
 - https://fontforge.org/docs/scripting/python.html
 - https://github.com/benob/png_font_to_ttf

Misc:
 - https://github.com/benob/png_font_to_ttf
 - https://github.com/pteromys/svgs2ttf/blob/master/svgs2ttf
 - https://github.com/sl2/TTF-to-PNG
 - https://stackoverflow.com/questions/12336401/creating-icon-fonts-with-vector-software-i-e-inkscape-and-fontforge
 - https://stackoverflow.com/questions/13278707/how-can-i-convert-svg-files-to-a-font
 - https://stackoverflow.com/questions/63380545/how-to-convert-a-set-of-images-into-a-font-ttf-file-with-python
 - https://stackoverflow.com/questions/63380545/how-to-convert-a-set-of-images-into-a-font-ttf-file-with-python
 - https://superuser.com/questions/1337567/how-do-i-convert-a-ttf-into-individual-png-character-images
 - https://superuser.com/questions/48879/how-can-i-make-a-font-using-a-png-image
 - https://web.archive.org/web/20170107170808/http://stackoverflow.com/questions/13882328/tools-to-convert-svg-to-ttf
 - https://stackoverflow.com/questions/27863832/calling-python-2-script-from-python-3
 - https://stackoverflow.com/questions/22124130/import-a-sequence-of-svg-files-into-fontforge-as-glyphs-and-output-a-font-file
 - https://itecnote.com/tecnote/python-import-a-sequence-of-svg-files-into-fontforge-as-glyphs-and-output-a-font-file/
 - https://www.youtube.com/watch?v=jKW2hf_RWT4
 - https://github.com/fontforge/fontforge/issues/4766
 - https://gist.github.com/psmay/fd3e7e91893f6012b262
 - https://stackoverflow.com/questions/631406/what-is-the-difference-between-em-dash-151-and-8212
 - https://stackoverflow.com/questions/8600552/python-get-character-code-in-different-encoding
 - https://www.obliquity.com/computer/html/unicode1D400.html
 - https://www.lennyfacecopypaste.com/text-symbols/circle-numbers.html
 - https://stackoverflow.com/questions/7291120/get-unicode-code-point-of-a-character-using-python
 - https://note.nkmk.me/en/python-chr-ord-unicode-code-point/
 - https://stackoverflow.com/questions/1273693/why-is-u-used-to-designate-a-unicode-code-point
 - https://github.com/fonttools/fontbakery/issues/1939
 - https://github.com/carrasti/pysvg2font
 - https://github.com/pteromys/svgs2ttf
 - https://fontforge.org/docs/faq.html
 - https://stackoverflow.com/questions/17097775/how-to-reference-to-other-glyphs-in-fontforge
 - https://help.fontlab.com/fontlab/7/manual/About-Glyphs/
 - https://github.com/benob/png_font_to_ttf
