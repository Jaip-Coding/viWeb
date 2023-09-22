class Tag:
    def __init__(self, tag_name, content="", **attributes):
        self.tag_name = tag_name
        self.content = content
        self.attributes = attributes

    def __str__(self):
        attribute_str = ""
        for key, value in self.attributes.items():
            attribute_str += f' {key}="{value}"'

        if self.content:
            content_str = ""
            for item in self.content:
                if isinstance(item, Tag):
                    content_str += str(item)
                else:
                    content_str += str(item)
            return f'<{self.tag_name}{attribute_str}>{content_str}</{self.tag_name}>'
        else:
            return f'<{self.tag_name}{attribute_str}>'


class viWeb:
    def __init__(self):
        self.head = None
        self.body = None

    def __str__(self):
        return f'<!DOCTYPE html>\n<html>\n{self.head}\n{self.body}\n</html>'


class Head(Tag):
    def __init__(self):
        super().__init__('head')
        self.content = []

    def __str__(self):
        content_str = ""
        for item in self.content:
            content_str += str(item)
        return f'<{self.tag_name}>\n{content_str}\n</{self.tag_name}>'

    def favicon(self, href, **attributes):
        return Favicon(href, **attributes)


class Favicon(Tag):
    def __init__(self, href, **attributes):
        attributes['rel'] = 'icon'
        attributes['type'] = 'image/x-icon'
        attributes['href'] = href
        super().__init__('link', '', **attributes)


class Body(Tag):
    def __init__(self):
        super().__init__('body')
        self.content = []

    def __str__(self):
        content_str = ""
        for item in self.content:
            content_str += str(item)
        return f'<{self.tag_name}>\n{content_str}</{self.tag_name}>'


class Title(Tag):
    def __init__(self, content=""):
        super().__init__('title', content)


class Heading(Tag):
    def __init__(self, level, content=""):
        super().__init__(f'h{level}', content)

    def bold(self, content):
        return Bold(content)

    def italic(self, content):
        return Italic(content)

    def marked(self, content):
        return Marked(content)

    def underline(self, content):
        return Underline(content)

    def strikethrough(self, content):
        return Strikethrough(content)

    def superscript(self, content):
        return Superscript(content)

    def subscript(self, content):
        return Subscript(content)

    def small(self, content):
        return Small(content)

    def horizontal_rule(self):
        return HorizontalRule()

    def line_break(self):
        return LineBreak()

    def image(self, src, alt="", **attributes):
        return Image(src, alt, **attributes)


class Paragraph(Tag):
    def __init__(self, content=""):
        super().__init__('p', content)

    def bold(self, content):
        return Bold(content)

    def italic(self, content):
        return Italic(content)

    def marked(self, content):
        return Marked(content)

    def underline(self, content):
        return Underline(content)

    def strikethrough(self, content):
        return Strikethrough(content)

    def superscript(self, content):
        return Superscript(content)

    def subscript(self, content):
        return Subscript(content)

    def small(self, content):
        return Small(content)

    def horizontal_rule(self):
        return HorizontalRule()

    def line_break(self):
        return LineBreak()

    def image(self, src, alt="", **attributes):
        return Image(src, alt, **attributes)


class Bold(Tag):
    def __init__(self, content=""):
        super().__init__('b', content)


class Italic(Tag):
    def __init__(self, content=""):
        super().__init__('i', content)


class Marked(Tag):
    def __init__(self, content=""):
        super().__init__('mark', content)


class Underline(Tag):
    def __init__(self, content=""):
        super().__init__('u', content)


class Strikethrough(Tag):
    def __init__(self, content=""):
        super().__init__('del', content)


class Superscript(Tag):
    def __init__(self, content=""):
        super().__init__('sup', content)


class Subscript(Tag):
    def __init__(self, content=""):
        super().__init__('sub', content)


class Small(Tag):
    def __init__(self, content=""):
        super().__init__('small', content)


class HorizontalRule(Tag):
    def __init__(self):
        super().__init__('hr', '')


class LineBreak(Tag):
    def __init__(self):
        super().__init__('br', '')


class Image(Tag):
    def __init__(self, src, alt="", **attributes):
        attributes['src'] = src
        attributes['alt'] = alt
        super().__init__('img', '', **attributes)


class Link(Tag):
    def __init__(self, href, content, **attributes):
        attributes['href'] = href
        super().__init__('a', content, **attributes)


class UnorderedList(Tag):
    def __init__(self, items, list_type='disc', **attributes):
        self.list_type = list_type
        self.items = items
        super().__init__('ul', '', **attributes)

    def __str__(self):
        attributes_str = ' '.join([f'{key}="{value}"' for key, value in self.attributes.items()])
        items_str = ''.join([f'<li>{item}</li>' for item in self.items])
        return f'<{self.tag_name} type="{self.list_type}" {attributes_str}>\n{items_str}\n</{self.tag_name}>'


class OrderedList(Tag):
    def __init__(self, items, list_type='1', **attributes):
        self.list_type = list_type
        self.items = items
        super().__init__('ol', '', **attributes)

    def __str__(self):
        attributes_str = ' '.join([f'{key}="{value}"' for key, value in self.attributes.items()])
        items_str = ''.join([f'<li>{item}</li>' for item in self.items])
        return f'<{self.tag_name} type="{self.list_type}" {attributes_str}>\n{items_str}\n</{self.tag_name}>'


class DescriptionList(Tag):
    def __init__(self, items, **attributes):
        self.items = items
        super().__init__('dl', '', **attributes)

    def __str__(self):
        attributes_str = ' '.join([f'{key}="{value}"' for key, value in self.attributes.items()])
        items_str = ''.join([f'<dt>{term}</dt><dd>{description}</dd>' for term, description in self.items])
        return f'<{self.tag_name} {attributes_str}>\n{items_str}\n</{self.tag_name}>'


class Audio(Tag):
    def __init__(self, src, autoplay=False, **attributes):
        self.src = src
        self.autoplay = autoplay
        super().__init__('audio', '', **attributes)

    def __str__(self):
        attributes_str = ' '.join([f'{key}="{value}"' for key, value in self.attributes.items()])
        autoplay_str = ' autoplay' if self.autoplay else ''
        audio_element = f'<source src="{self.src}" type="audio/mpeg">' \
                        f'Your browser does not support the audio element.'
        return f'<{self.tag_name} controls{autoplay_str} {attributes_str}>\n{audio_element}\n</{self.tag_name}>'



class Video(Tag):
    def __init__(self, src, width=None, height=None, autoplay=False, controls=True, **attributes):
        self.src = src
        self.width = width
        self.height = height
        self.autoplay = autoplay
        self.controls = controls
        super().__init__('video', '', **attributes)

    def __str__(self):
        attributes_str = ' '.join([f'{key}="{value}"' for key, value in self.attributes.items()])
        autoplay_str = ' autoplay' if self.autoplay else ''
        controls_str = ' controls' if self.controls else ''
        width_str = f' width="{self.width}"' if self.width else ''
        height_str = f' height="{self.height}"' if self.height else ''
        video_element = f'<source src="{self.src}" type="video/mp4">' \
                        f'Your browser does not support the video element.'
        return f'<{self.tag_name}{controls_str}{autoplay_str}{width_str}{height_str}{attributes_str}>\n{video_element}\n</{self.tag_name}>'