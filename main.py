import fancy_text

print(fancy_text.parse_bb_simple("[b]bold[/b]...[i]italic[/i]...[pre]monospace[/pre]"))
exit()
text = input("Type a text: ")
print(text)
for font in fancy_text.fonts_list:
    print('{}: {}'.format(font.name, fancy_text.apply(font, text)))

print(fancy_text.apply_fontname(fancy_text.get_font("bold"), text))
print(fancy_text.apply_fontname(fancy_text.get_font("aaa"), text))
