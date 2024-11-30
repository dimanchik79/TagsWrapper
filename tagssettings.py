
TAGS = {
        'div': ('<div*style*>', '</div>'),
        'span': ('<span*style*>', '</span>'),
        'b': ('<b*style*>', '</b>'),
        'i': ('<i*style*>', '</i>'),
        'hr': ('<hr>', ''),
        'br': ('<br>', ''),
        'sup': ('<span class="sup"*style*>', '</span>'),
        'sub': ('<span class="sub"*style*>', '</span>'),
        'tleft': ('<div align="left"*style*>', '</div>'),
        'tcenter': ('<div align="center"*style*>', '</div>'),
        'tjustify': ('<div align="justify"*style*>', '</div>'),
        'tright': ('<div align="right"*style*>', '</div>'),
        'li': ('<li*style*>', '</li>'),
        'tr': ('<tr*style*>', '</tr>'),
        'th': ('<th*style*>', '</th>'),
        'td': ('<td*style*>', '</td>'),

        'p': ('<p*style*>', '</p>'),
        'ul': ('<ul style="text-indent: 0;*style*">', '</ul>'),
        'table': ('<table*style*>\n<thead>\n<tr>\n\n</tr>\n</thead>\n<tbody>\n<tr>\n\n</tr>\n', '</tbody>\n</table>'),
        'ulli': ('<li*style*>', '</li>'),
        }

HELP = {
        'RU': 'Программа предназначена для оборачивания простого текста в html-тэги. Так-то тут все понятно: вставляешь текст, выделяешь фрагмент и жмешь на кнопку нужного тега. Если, вдруг, накосячили - жмём два раза CTRL-z или на кнопочки с круглыми стрелочками. Результат работы можно сохранить в текстовый файл wrapper.txt по заранее выбранному пути',
        'ENG': 'The program is designed to wrap plain text in html tags. So everything is clear here: you insert the text, select the fragment and click on the button of the desired tag. If, suddenly, you mess up, press CTRL-z twice or on the buttons with round arrows. The result of the work can be saved to a text file wrapper.txt by a pre-selected path',
        }