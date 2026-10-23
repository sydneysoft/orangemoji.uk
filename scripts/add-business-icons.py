"""Generate new OrangeMoji icons (color + line) in the set's existing style: 72x72, orange #E85D04 fills,
#1C1917 outlines, #FFF6EE highlights; line variant uses currentColor."""
import json, sys
from pathlib import Path
O, D, L = "#E85D04", "#1C1917", "#FFF6EE"
# element: (tag, attrs, role, stroke_width) role: o orange, l light, n stroke only, d dark fill
ICONS = {
 "truck": ("places", ["truck", "lorry", "transport", "freight", "fleet"], [
   ("rect", 'x="8" y="20" width="34" height="26" rx="3"', "o", 2.4),
   ("path", 'd="M42 28h11l9 10v8H42z"', "l", 2.4),
   ("path", 'd="M46 31h6l5 6h-11z"', "n", 1.8),
   ("path", 'd="M8 46h54"', "n", 2.4),
   ("circle", 'cx="20" cy="50" r="5"', "d", 0),
   ("circle", 'cx="52" cy="50" r="5"', "d", 0)]),
 "route": ("places", ["route", "trip", "journey", "path", "dispatch"], [
   ("path", 'd="M18 54c0-10 36-6 36-18S30 26 30 18"', "n", 2.4),
   ("circle", 'cx="18" cy="56" r="6"', "o", 2.4),
   ("path", 'd="M30 30s9-9 9-15a9 9 0 1 0-18 0c0 6 9 15 9 15z"', "o", 2.4),
   ("circle", 'cx="30" cy="15" r="3"', "l", 1.8)]),
 "wrench": ("interface", ["wrench", "maintenance", "repair", "mechanic", "workshop"], [
   ("path", 'd="M46 12a12 12 0 0 0-11 16L14 49a5 5 0 0 0 7 7l21-21a12 12 0 0 0 16-11l-7 4-6-4-1-7z"', "o", 2.4),
   ("circle", 'cx="18" cy="52" r="2"', "l", 1.6)]),
 "person": ("faces", ["person", "user", "profile", "employee", "driver"], [
   ("circle", 'cx="36" cy="24" r="11"', "o", 2.4),
   ("path", 'd="M14 60c2-12 11-18 22-18s20 6 22 18z"', "o", 2.4),
   ("path", 'd="M31 22h0M41 22h0"', "n", 3)]),
 "people": ("faces", ["people", "team", "staff", "human resources", "hr"], [
   ("circle", 'cx="48" cy="24" r="8"', "l", 2.2),
   ("path", 'd="M38 44c2-6 6-9 10-9 8 0 12 6 13 14H44"', "l", 2.2),
   ("circle", 'cx="28" cy="26" r="10"', "o", 2.4),
   ("path", 'd="M8 60c2-11 10-16 20-16s18 5 20 16z"', "o", 2.4)]),
 "calendar": ("interface", ["calendar", "date", "schedule", "planning"], [
   ("rect", 'x="12" y="16" width="48" height="44" rx="6"', "l", 2.4),
   ("path", 'd="M12 22a6 6 0 0 1 6-6h36a6 6 0 0 1 6 6v8H12z"', "o", 2.4),
   ("path", 'd="M24 10v10M48 10v10"', "n", 2.4),
   ("rect", 'x="22" y="38" width="8" height="8" rx="1.5"', "d", 0),
   ("path", 'd="M38 42h12M22 52h28"', "n", 2)]),
 "document": ("interface", ["document", "file", "page", "contract", "licence"], [
   ("path", 'd="M18 8h26l12 12v42a4 4 0 0 1-4 4H18a4 4 0 0 1-4-4V12a4 4 0 0 1 4-4z"', "l", 2.4),
   ("path", 'd="M44 8v12h12"', "o", 2.4),
   ("path", 'd="M24 32h24M24 41h24M24 50h16"', "n", 2.2)]),
 "layout": ("interface", ["layout", "sections", "page builder", "blocks", "template"], [
   ("rect", 'x="10" y="10" width="52" height="52" rx="6"', "l", 2.4),
   ("rect", 'x="16" y="16" width="40" height="12" rx="2"', "o", 2),
   ("rect", 'x="16" y="34" width="18" height="22" rx="2"', "o", 2),
   ("path", 'd="M40 36h16M40 45h16M40 54h10"', "n", 2.2)]),
 "form": ("interface", ["form", "contact", "fields", "input", "survey"], [
   ("rect", 'x="12" y="8" width="48" height="56" rx="6"', "l", 2.4),
   ("rect", 'x="19" y="17" width="34" height="9" rx="2"', "n", 2),
   ("rect", 'x="19" y="32" width="34" height="9" rx="2"', "n", 2),
   ("rect", 'x="19" y="48" width="18" height="9" rx="3"', "o", 2)]),
 "inbox": ("interface", ["inbox", "messages", "submissions", "tray"], [
   ("path", 'd="M10 40l8-24h36l8 24v14a6 6 0 0 1-6 6H16a6 6 0 0 1-6-6z"', "l", 2.4),
   ("path", 'd="M10 40h14l4 7h16l4-7h14v14a6 6 0 0 1-6 6H16a6 6 0 0 1-6-6z"', "o", 2.4)]),
 "rocket": ("symbols", ["rocket", "start", "launch", "go"], [
   ("path", 'd="M36 8c10 8 14 20 12 34H24C22 28 26 16 36 8z"', "o", 2.4),
   ("circle", 'cx="36" cy="26" r="5"', "l", 2),
   ("path", 'd="M24 34l-8 10v8l8-6M48 34l8 10v8l-8-6"', "l", 2.2),
   ("path", 'd="M30 48c0 6 3 10 6 14 3-4 6-8 6-14"', "d", 0)]),
 "no-entry": ("symbols", ["no entry", "cancel", "stop", "forbidden", "retire"], [
   ("circle", 'cx="36" cy="36" r="24"', "o", 2.4),
   ("rect", 'x="20" y="32" width="32" height="8" rx="2"', "l", 2)]),
 "eye-off": ("interface", ["hide", "unpublish", "hidden", "private"], [
   ("path", 'd="M8 36s10-16 28-16 28 16 28 16-10 16-28 16S8 36 8 36z"', "l", 2.4),
   ("circle", 'cx="36" cy="36" r="8"', "o", 2.2),
   ("path", 'd="M14 14l44 44"', "n", 3)]),
 "archive": ("interface", ["archive", "box", "store", "history"], [
   ("rect", 'x="10" y="14" width="52" height="12" rx="3"', "o", 2.4),
   ("path", 'd="M14 26h44v28a6 6 0 0 1-6 6H20a6 6 0 0 1-6-6z"', "l", 2.4),
   ("path", 'd="M29 36h14"', "n", 3)]),
 "clock": ("interface", ["clock", "time", "history", "eta"], [
   ("circle", 'cx="36" cy="36" r="24"', "l", 2.4),
   ("path", 'd="M36 22v14l10 6"', "n", 3),
   ("circle", 'cx="36" cy="36" r="3"', "d", 0)]),
 "history": ("interface", ["history", "traceability", "changes", "audit", "log"], [
   ("path", 'd="M14 36a22 22 0 1 0 6-15"', "n", 2.4),
   ("path", 'd="M12 12v12h12"', "o", 2.4),
   ("path", 'd="M36 24v12l9 6"', "n", 3),
   ("circle", 'cx="36" cy="36" r="3"', "d", 0)]),
 "shield": ("symbols", ["shield", "security", "captcha", "protection", "guard"], [
   ("path", 'd="M36 8l22 8v16c0 14-9 25-22 32-13-7-22-18-22-32V16z"', "o", 2.4),
   ("path", 'd="M26 36l7 7 13-14"', "l", 3)]),
 "building": ("places", ["building", "company", "organization", "office", "tenant"], [
   ("rect", 'x="14" y="10" width="30" height="52" rx="3"', "o", 2.4),
   ("rect", 'x="44" y="28" width="16" height="34" rx="2"', "l", 2.2),
   ("path", 'd="M22 20h4M32 20h4M22 30h4M32 30h4M22 40h4M32 40h4"', "n", 2.6),
   ("rect", 'x="25" y="50" width="8" height="12"', "d", 0)]),
 "fuel": ("places", ["fuel", "petrol", "diesel", "gas station"], [
   ("rect", 'x="12" y="12" width="30" height="48" rx="4"', "o", 2.4),
   ("rect", 'x="18" y="18" width="18" height="12" rx="2"', "l", 2),
   ("path", 'd="M42 26h6l6 6v20a4 4 0 0 1-8 0V40h-4"', "n", 2.4),
   ("path", 'd="M8 60h38"', "n", 2.4)]),
 "wallet": ("symbols", ["wallet", "payment", "money", "cash", "billing"], [
   ("path", 'd="M12 22a6 6 0 0 1 6-6h34v8"', "n", 2.4),
   ("rect", 'x="10" y="22" width="52" height="36" rx="6"', "o", 2.4),
   ("rect", 'x="42" y="34" width="20" height="12" rx="4"', "l", 2.2),
   ("circle", 'cx="49" cy="40" r="2.4"', "d", 0)]),
 "map": ("places", ["map", "tracking", "gps", "location", "live map"], [
   ("path", 'd="M10 18l16-6 20 6 16-6v42l-16 6-20-6-16 6z"', "l", 2.4),
   ("path", 'd="M26 12v42M46 18v42"', "n", 2),
   ("path", 'd="M36 44s8-8 8-14a8 8 0 1 0-16 0c0 6 8 14 8 14z"', "o", 2.2),
   ("circle", 'cx="36" cy="30" r="2.6"', "l", 1.6)]),
 "dashboard": ("interface", ["dashboard", "reports", "analytics", "overview"], [
   ("rect", 'x="10" y="12" width="52" height="48" rx="6"', "l", 2.4),
   ("rect", 'x="18" y="38" width="8" height="14" rx="1.5"', "o", 2),
   ("rect", 'x="32" y="28" width="8" height="24" rx="1.5"', "o", 2),
   ("rect", 'x="46" y="20" width="8" height="32" rx="1.5"', "o", 2)]),
}

def el(tag, attrs, role, sw, line):
    if line:
        fill = 'fill="currentColor"' if role == "d" else ""
        stroke = f'stroke="currentColor" stroke-width="{sw}"' if sw else ""
    else:
        fill = {"o": f'fill="{O}"', "l": f'fill="{L}"', "d": f'fill="{D}"', "n": ""}[role]
        stroke = f'stroke="{D}" stroke-width="{sw}"' if sw else ""
    parts = " ".join(p for p in (attrs, fill, stroke) if p)
    return f"  <{tag} {parts}/>"

def svg(items, line):
    head = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 72 72" fill="none" stroke-linecap="round" stroke-linejoin="round">'
    return "\n".join([head] + [el(*i, line) for i in items] + ["</svg>"])

root = Path(sys.argv[1])
raw = (root / "orangemoji.json").read_text()
catalog = json.loads(raw)
names = {c["name"] for c in catalog}
for name, (category, tags, items) in ICONS.items():
    assert name not in names, name
    (root / "icons/color" / f"{name}.svg").write_text(svg(items, False))
    (root / "icons/line" / f"{name}.svg").write_text(svg(items, True))
    catalog.append({"name": name, "category": category, "tags": tags, "color": svg(items, False), "line": svg(items, True)})
(root / "orangemoji.json").write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + ("\n" if raw.endswith("\n") else ""))
print(len(ICONS), "icons added;", len(catalog), "total")
