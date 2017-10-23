#!/bin/bash

curl -s http://www.studentenwerk-marburg.de/essen-trinken/speiseplan/heute.html | sed -n '/Mensa Lahnberge/,/Philipps Bistro/p' | sed -n '/<td class="col1">/,/<\/td>/p' | sed -n '/<td class="col2">/,/<\/td>/p' | sed 's/\s\+<td class="col2">\|<\/td>//'
