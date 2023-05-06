# fancy-text

Based on [Secret-chest/fancy-text](https://github.com/Secret-chest/fancy-text). Checkout also [Secret-chest/fancify-text](https://github.com/Secret-chest/fancify-text). 

A simple Python program to convert your text to Unicode fonts that work anywhere with basic bbcode support

## Usage

```
import fancy_text

print(fancy_text.parse_bb_simple("[b]bold[/b]...[i]italic[/i]...[pre]monospace[/pre]"))

> 𝗯𝗼𝗹𝗱...𝘪𝘵𝘢𝘭𝘪𝘤...ｍｏｎｏｓｐａｃｅ
```
see also `main.py`

## Fonts:
- 𝗕𝗼𝗹𝗱
- 𝘐𝘵𝘢𝘭𝘪𝘤
- 𝘽𝙤𝙡𝙙 𝙄𝙩𝙖𝙡𝙞𝙘
- Ｍｏｎｏｓｐａｃｅｄ
- Typewriter
- 𝐒𝐞𝐫𝐢𝐟
- 𝓗𝓪𝓷𝓭𝔀𝓻𝓲𝓽𝓲𝓷𝓰
- 𝕱𝖔𝖗𝖒𝖆𝖑
- 🇧 🇱 🇺 🇪 (this is uppercase-only!)
- 🅂🅀🅄🄰🅁🄴🄳 (also uppercase-only)
- 🅒🅘🅡🅒🅛🅔🅓 (also uppercase-only)
- sᴍᴀʟʟ ᴄᴀᴘs
- ᑕOOᒪ ᕼᗩᑎᗪᗯᖇITIᑎG (uppercase-only, thanks To @WorldLanguages for the Scratch Symbols project)
- ᗡƎƧЯƎVƎЯ (uppercase-only)
- uʍop ǝpᴉsd∩
- 匚ㄖㄖㄥ ㄒ乇乂ㄒ (also uppercase-only)
- 𝕆𝕦𝕥𝕝𝕚𝕟𝕖
- ƈųཞƖყ (this is lowercase-only!)
- ɦαɳ∂ω૨เƭเɳɠ 3 (also lowercase-only)
- ʂƚɾαɳɠҽ (also lowercase-only)
- ƈųཞƖყ (uppercase-only!)
- ɦαɳ∂ω૨เƭเɳɠ 3 (lowercase-only)
- ɱαɠιƈ (lowercase only!)
- ๓คﻮเς 2 (also lowercase-only)
- ડ𝕥𝕣ꪖꪀᧁꫀ (lowercase only)
- 🄟🄐🄡🄐🄝🄣🄗🄔🄢🄘🄩🄔🄓 (uppercase-only)
- 🅱🅾🆇🅴🅳 (also uppercase-only!)

### Note:
Lowercase letters will be automatically replaced with uppercase ones when you use an uppercase-only font (This also applies to lowercase-only fonts!).

## Character support:
Most fonts support only the alphabet, some support the alphabet + numbers, Monospaced supports ASCII.
