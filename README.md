# amrabdelbari.github.io

Personal profile site of Amr Abdelbari, served by GitHub Pages, in three languages:

- English: `/` (`index.html`)
- Arabic (RTL): `/ar/`
- Turkish: `/tr/`

## Editing

The three pages are generated from one template so they stay in sync:

- `build/i18n.py`: all page text, per language
- `build/build.py`: layout, publication list and profile links
- `build/graphics.py`: icons and animated project illustrations (inline SVG)
- `assets/site.css`, `assets/arena.js`, `assets/site.js`: shared styles, the arena animation, scroll reveal and count-up
- `assets/photo.jpg`: profile photo (square, about 400×400 px). Until it exists the page shows initials.

After editing, run `python3 build/build.py` and commit the regenerated HTML.
