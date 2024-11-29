
TAGS = {
        'div': ('<div*style*>', '</div>'),
        'span': ('<span*style*>', '</span>'),
        'b': ('<b*style*>', '</b>'),
        'i': ('<i*style*>', '</i>'),
        'hr': ('<hr>', ''),
        'br': ('<br>', ''),
        'sup': ('<span class="sup"*style*>', '</span>'),
        'sub': ('<span class="sub"*style*>', '</span>'),
        'tleft': ('<span align="left"*style*>', '</span>'),
        'tcenter': ('<span align="center"*style*>', '</span>'),
        'tjustify': ('<span align="justify"*style*>', '</span>'),
        'tright': ('<span align="right"*style*>', '</span>'),
        'li': ('<li*style*>', '</li>'),
        'tr': ('<tr*style*>', '</tr>'),
        'th': ('<th*style*>', '</th>'),
        'td': ('<td*style*>', '</td>'),

        'p': ('<p style="text-indent: 25px;*style*">', '</p>'),
        'ul': ('<ul style="text-indent: 0;*style*">', '</ul>'),
        'table': ('<table*style*>\n<thead>\n<tr>\n\n</tr>\n</thead>\n<tbody>\n<tr>\n\n</tr>\n', '</tbody>\n</table>'),
        'ulli': ('<li*style*>', '</li>'),
        }

SETTINGS = {
        'dir': None,
        'style': None,
        'idl': None,
        'ids': None,
        'txt': None,
        }