import re
import sys

fonts_list = []


class Font:
    name: str
    source: str
    target: str
    uppercaseOnly: bool
    needSpaces: bool  # https://jkorpela.fi/chars/spaces.html

    def __init__(self, _name: str, _source: str, _target: str, _uppercase_only=False, _need_spaces=False):
        self.name = _name
        self.source = _source
        self.target = _target
        self.uppercaseOnly = _uppercase_only
        self.needSpaces = _need_spaces
        fonts_list.append(self)


class Fonts:
    bold = Font('bold',
                'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789',
                '𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵')
    italic = Font('italic',
                  'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789',
                  '𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫')
    bold_italic = Font('bold_italic',
                       'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789',
                       '𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵')
    monospace = Font('monospace',
                     'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!"#$%&\'()*+,-./0123456789:;<=>?@[\\]^_`{|}~',
                     'ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ！＂＃＄％＆＇（）＊＋，－．／０１２３４５６７８９：；＜＝＞？＠［＼］＾＿｀｛｜｝～')
    typewriter = Font('typewriter',
                      'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789',
                      '𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿')
    serif = Font('serif',
                 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789',
                 '𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗')

    handwriting = Font('handwriting',
                       'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                       '𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃')
    handwriting_2 = Font('handwriting_2',
                         'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                         'ᗩᗷᑕᗪEᖴGᕼIᒍKᒪᗰᑎOᑭᑫᖇᔕTᑌᐯᗯ᙭Yᘔ',
                         True)
    handwriting_3 = Font('handwriting_3',
                         'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                         'αɓ૮∂εƒɠɦเʝҡℓɱɳσρզ૨รƭµѵωאყƶ',
                         True)
    handwriting_4 = Font('handwriting_4',
                         'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                         '𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒥𝒦𝐿𝑀𝒩𝓞𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏')

    formal = Font('formal',
                  'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                  '𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟')

    outline = Font('outline',
                   'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890',
                   '𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘')

    small_caps = Font('small_caps',
                      'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                      'ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ',
                      True)

    blue = Font('blue',
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ ',
                '🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿 ',
                True, True)

    squared = Font('squared',
                   'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                   '🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉',
                   True)
    circled = Font('circled',
                   'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                   '🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩',
                   True)
    boxed = Font('boxed',
                 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                 '🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉',
                 True)

    reversed = Font('reversed',
                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                    'AᗺƆᗡƎꟻວHIᒐꓘ⅃MИOꟼϘЯƧTUVWXYZ',
                    True)
    upside_down = Font('upside_down',
                       'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                       '∀ᗺƆᗡƎℲפHIſꓘ˥WNOԀQɹS┴∩ΛMX⅄Zɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz'),
    cool_text = Font('cool_text',
                     'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                     '卂乃匚ᗪ乇千Ꮆ卄丨ﾌҜㄥ爪几ㄖ卩Ɋ尺丂ㄒㄩᐯ山乂ㄚ乙',
                     True)
    curly = Font('curly',
                 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                 'ąცƈɖɛʄɠɧıʝƙƖɱŋơ℘զཞʂɬų۷ῳҳყʑ',
                 True)
    magic = Font('magic',
                 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                 'αႦƈԃҽϝɠԋιʝƙʅɱɳσρϙɾʂƚυʋɯxყȥ',
                 True)
    magic_2 = Font('magic_2',
                   'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                   'ค๒ς๔єŦﻮђเןкɭ๓ภ๏קợгรՇยשฬץאչ',
                   True)
    strange = Font('strange',
                   'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                   'ꪖ᥇ᥴᦔꫀᠻᧁꫝⅈ𝕛𝕜ꪶꪑꪀꪮρ𝕢𝕣ડ𝕥ꪊꪜ᭙᥊ꪗ𝕫',
                   True)
    parenthesized = Font('parenthesized',
                         'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                         '🄐🄑🄒🄓🄔🄕🄖🄗🄘🄙🄚🄛🄜🄝🄞🄟🄠🄡🄢🄣🄤🄥🄦🄧🄨🄩',
                         True)


def get_font(fontname: str) -> Font:
    for font in fonts_list:
        if font.name == fontname:
            return font
    exit("font '{}' not found".format(fontname))


def apply(font: Font, text: str) -> str:
    if font.uppercaseOnly:
        text = text.upper()

    result = ''
    for char in text:
        if char in font.source:
            index = font.source.index(char)
            result += font.target[index]
            if font.needSpaces:
                result += '​'
        else:
            result += char

    return result


def parse_bb_simple(text: str) -> str:
    """
    see https://www.bbcode.org/reference.php
    only supports [b], [i] and [pre]
    does not support nesting
    :param text:
    :return:
    """

    def code_pattern(c: str):
        return '\[{}\]([^\[/]+)\[/{}\]'.format(c, c)

    text = re.sub(code_pattern('b'), lambda x: apply(Fonts.bold, x.group(1)), text)
    text = re.sub(code_pattern('i'), lambda x: apply(Fonts.italic, x.group(1)), text)
    text = re.sub(code_pattern('pre'), lambda x: apply(Fonts.monospace, x.group(1)), text)
    return text


if __name__ == '__main__':
    if sys.argv[1] == "bb":
        print(parse_bb_simple(sys.argv[2]))
