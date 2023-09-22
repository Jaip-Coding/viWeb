# viWeb-v1.0
viWeb (VisualWebdevelopment) is a tool for building websites with Python.

## About
viWeb is a tool to write HTML code with Python. viWeb provides all important tags in HTML.

## Instructions
A short guide for viWeb 1.0

### Head
Create a new document. You can call it „example.viw.“ Access viWeb with ``` viWeb = viWeb() ```. Then create the head of the website as follows:
```
viWeb = viWeb()
viWeb.head = Head()
viWeb.head.content = [
    Title("My Website"),
    viWeb.head.favicon("favicon.ico")
]
```
Adjust the title and the favicon.

### Body
Create the body with ``` viWeb.body = Body() ```
Then create the list ``` content ``` and insert the content of the website there. Here is an example:
```
content = [
    Heading(1, "Welcome!"),
    Paragraph("This is my Website")
]
```
Don’t forget the commas!

Finally, write ``` viWeb.body.content = content ```
This adds ```content``` to your website.

## Execute code
To execute your code, go to ``` main.py ```
Change „example.viw“ to the name of your document: ``` with open('example.viw', 'r') as file: ```

Change „index.html“ to the name of the HTML file to be created: ``` with open('index.html', 'w') as file: ```

Run main.py. An HTML file will be created.
Now run this HTML file.

## Commands
A list of all commands:

### Heading
Example: ``` Heading(1, "Hello") ``` or ``` Heading(6, ["This is a ", Marked("cool"), "website"]) ```

Available commands:
```Bold()```
```Italic()```
```Underline()```
```Marked()```
```Strikethrough()```
```Superscript()```
```Subscript()```
```Small()```

### Paragraph
Example: ```Paragraph("This is a text") ``` or ```Paragraph(["This is a ", Bold("cool"), "website"])```

Available commands:
```Bold()```
```Italic()```
```Underline()```
```Marked()```
```Strikethrough()```
```Superscript()```
```Subscript()```
```Small()```
```Link()```

### Image
Example: ```Image("image.jpg", alt="A sample image")``` or ```Image("https://example.com/image.png", alt="A sample image", width="300", height="200")```

### UnorderedList
Example: ```UnorderedList(["Item 1", "Item 2", "Item 3"], list_type='circle') ```

You can change ```list_style ``` to „circle“ or „square“ or delete it.

### OrderedList
Example: ```OrderedList(["First item", "Second item", "Third item"], list_type='I')```

List types: „A“, „a“, „I“, „i“

### DescriptionList
Example: ```DescriptionList([("Term 1", "Description 1"), ("Term 2", "Description 2")])```

### Link
Example: ```Link("https://www.example.com", "A link")```

Can be used in Paragraph()

### Audio
Example: ```Audio("audio.mp3", autoplay=True)``` or ```Audio("https://example.com/audio.mp3", autoplay=False)```

### Video
Example: ```Video("video.mp4", width="640", height="360", autoplay=True, controls=True)``` or ```Video("https://example.com/video.mp4", width="160", height="90", autoplay=False, controls=True)```

### HorizontalRule
Example: ```HorizontalRule()```

### LineBreak
Example: ```LineBreak()```
