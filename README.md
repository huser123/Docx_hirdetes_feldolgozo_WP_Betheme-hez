# DOCX Fájl Feldolgozó HR Beszúrással

Ez a Python script az aktuális könyvtárban található `.docx` fájlokat dolgozza fel, megkeresi az `IDEIS` kulcsszót, és a következő műveleteket végzi:

1. Eltávolítja az `IDEIS` kulcsszót a szövegből.
2. Beszúr egy sort `[hr height=30 style=default line=default themecolor=1]` minden `IDEIS`-t tartalmazó bekezdés után.
3. Kilistázza az összes `.docx` fájlt a jelenlegi könyvtárban, lehetőséget adva a felhasználónak egy fájl kiválasztására.
4. A módosított tartalmat megjeleníti a terminálban.
5. Törli a konzol képernyőjét az operációs rendszer alapján (Windows vagy Linux/macOS).

## Főbb funkciók
- Automatikusan felismeri a jelenlegi könyvtárban található `.docx` fájlokat.
- Lehetőséget ad a felhasználónak egy fájl kiválasztására.
- A fájlokat az `IDEIS` kulcsszó eltávolításával és formázott sorok beszúrásával dolgozza fel.
- A módosított tartalmat közvetlenül a terminálban jeleníti meg.
- Zökkenőmentesen működik Windows, Linux és macOS rendszereken.

## Követelmények
- Python 3.6 vagy újabb verzió
- `python-docx` könyvtár

A szükséges könyvtár telepítése:
```bash
pip install python-docx
```

## Használat
1. Töltsd le a scriptet vagy klónozd a repository-t.
2. Helyezd el a feldolgozni kívánt `.docx` fájlokat a script könyvtárában.
3. Futtasd a scriptet:
   ```bash
   py hirdetes.py
   ```
4. A felsorolt fájlok közül válaszd ki a feldolgozni kívántat egy szám megadásával.
5. A módosított tartalom megjelenik a terminálban.

## Példa kimenet
Ha a `.docx` fájl a következő szöveget tartalmazza:

```
Ez egy példa bekezdés.
IDEIS Ez a bekezdés tartalmazza a kulcsszót.
Egy másik normál bekezdés.
```

A script kimenete:

```
Ez egy példa bekezdés.
Ez a bekezdés tartalmazza a kulcsszót.
[hr height=30 style=default line=default themecolor=1]
Egy másik normál bekezdés.
```

## Képernyő törlése
A script a konzol képernyőjét törli, mielőtt kilistázná a `.docx` fájlokat:
- Windows rendszeren a `cls` parancsot használja.
- Linux/macOS rendszeren a `clear` parancsot alkalmazza.

## Köszönetnyilvánítás
Köszönet a `python-docx` könyvtárnak, amely megkönnyíti a `.docx` fájlok kezelését Pythonban.

