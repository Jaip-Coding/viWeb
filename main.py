from viweb import viWeb, Head, Body, Title, Heading, Paragraph, Bold, Italic, Marked, Underline, Strikethrough, \
    Superscript, Subscript, Small, HorizontalRule, LineBreak, Image, Link, UnorderedList, OrderedList, DescriptionList, \
    Audio, Video, Favicon

with open('example.viw', 'r') as file:
    content = file.read()

exec(content)

html_content = str(viWeb)

with open('index.html', 'w') as file:
    file.write(html_content)
