## Let's hack the [Twilight Eve's](https://tever.xyz/) save-load system!  

Primarily a learning-focused project that leverages a handful of tools including:
- [Brython](https://brython.info/) (client-side python web scripting)
- [Tailwindcss](https://tailwindcss.com/) (html-oriented CSS framework)
- [HxD](https://mh-nexus.de/en/hxd/) editor for low-level data manipulation  
*and others*

### Current state of production
- [x] [Cut through TeveF's map protection and got to map's internal infrastructure.](original/war3map_refactored_1.j)
- [x] [Decoded](src/utilities/translation.py) and replicated the save-load functionality.
- [x] [Implemented an intuitive Python API wrapper for dealing with the save codes.](src/tevehack.py)
- [x] [Extracted and decoded](src/utilities/script.py) the binary resource files with **character**, **spell** and **item names** to complement the future GUI.
- [x] Created a [web-based GUI](https://PteNiX.github.io/laughing-engine) for simple user interaction, save-code loading, editing and generation.

Python API simplicity and convenience:
```py
hero = load('3PxA-a)Ek-U*6[-WQnm234234-d7Qa-yFpU-<PU3-Z5ep-q<C')
hero.heroXP = 99999999
hero.locationX = -10000
hero.locationY = 8000
code = save(hero, 'Fingon')
if code: print('-load ' + code)

res = load('kEF5-2d+d-o2<L-hW<T-R>D?-faQV-wU>U->]Bh-(Q*x-r<)N-TQX')
res.gold = 9999999
res.lumber = 300
code2 = save(res, 'Fingon')
if code2: print('-load2 ' + code2)
```
