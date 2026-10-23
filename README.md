# OrangeEmoji

Open icons for designers, developers and everyone else. An OrangeSoft project.

Site: https://orangemoji.uk
Package: https://www.npmjs.com/package/orangemoji

## Use

```bash
npm install orangemoji
```

Import files through your bundler (Vite, webpack):

```jsx
import bookUrl from "orangemoji/icons/color/book.svg";

<img src={bookUrl} width={32} height={32} alt="" />
```

CDN:

```html
<img src="https://cdn.jsdelivr.net/npm/orangemoji@1/icons/color/book.svg" width="32" height="32" alt="" />
```

Line icons live in `icons/line/` and use `currentColor`. That only works when the SVG is inline in your page; inside an `<img>` they draw black. To tint one from a URL, use it as a mask:

```html
<span style="display:inline-block; width:24px; height:24px; background:#E85D04;
  mask:url(https://orangemoji.uk/icons/line/terminal.svg) center / contain no-repeat"></span>
```

## License

CC BY 4.0. Credit OrangeEmoji / OrangeSoft. See LICENSE.txt.

## Business and transport icons (Oct 2026)

Twenty-two icons were added for OrangeSoft's ERP modules (fleet, trips, HR, payments, site builder, traceability):
`truck`, `route`, `wrench`, `person`, `people`, `calendar`, `document`, `layout`, `form`, `inbox`, `rocket`,
`no-entry`, `eye-off`, `archive`, `clock`, `history`, `shield`, `building`, `fuel`, `wallet`, `map`, `dashboard`.
They follow the set's rules (72×72, orange `#E85D04` fills, `#1C1917` outlines, `#FFF6EE` highlights; line variants
in `currentColor`) and are produced by `scripts/add-business-icons.py`, which also appends them to `orangemoji.json`.
Not yet published to npm; publishing is the owner's decision.
