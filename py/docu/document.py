#! /usr/bin/env python
# -*- coding:utf-8 -*-

# Real text editors use a binary-tree based data structure called a `rope` to
# model their document contents.

class Document:
    """"""
    def __init__(self):
        """"""
        # We might start with a `str` for the `Document` contests, but in
        # Python, strings aren't mutable. We can't insert a character into
        # it or remove one without creating a brand new string object. That
        # would be leaving a lot of `str` objects taking up memory until
        # Python's garbage collector sees fit to clean up behind us.

        # So, instead of a string, we'll use a LIST of characters, which
        # we can modify at will.
        self.characters = []
        # In addition, a `Document` class would need to know the current
        # cursor position within the list.
        # self.cursor = 0
        self.cursor = Cursor(self)
        # and should probably also store a filename for the document.
        self.filename = ''

    def insert(self, character):
        """"""
        # self.characters.insert(self.cursor, character)
        # self.cursor += 1
        if not hasattr(character, 'character'):
            character = Character(character)

        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()


    def delete(self):
        """"""
        # del self.characters[self.cursor]
        del self.characters[self.cursor.position]

    def save(self):
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))

    @property
    def string(self):
        """Since we've been using that stirng `join` fucntion a lot
        (to concatenate the characters so we can see the actual document
        contents), we can add a property to the `Document` class to give
        us the complete string."""
        # return "".join(self.characters)

        # modify the string property on `Document` to accept the new
        # `Character` values. All we need to do is call str() on each
        # character before we join it.
        return "".join((str(c) for c in self.characters))
    # def forward(self):
    #     """"""
    #     self.cursor += 1

    # def back(self):
    #     """"""
    #     self.cursor -= 1


class Cursor:
    """Let us turn the cursor attribute into an object that is aware of its
    position and can manipulate that position.

    We can move the forward and back methods to that calss, and a couple
    more for the `Home` and 'End` keys."""
    def __init__(self, document):
        """"""
        self.document = document
        self.position = 0

    def forward(self):
        """"""
        self.position += 1

    def back(self):
        """"""
        self.position -= 1

    def home(self):
        """"""
        # self.document.characters[self.positon-1] == '\n' means the cursor's
        # position has already been in the beginning of the line, which is
        # exactly the `Home` position. If not, move cursor back to THAT
        # position.

        # while not (self.document.characters[self.position-1] == '\n'):
        while not (self.document.characters[self.position-1].character
                   == '\n'):
            self.position -= 1
            if self.position == 0:
                # Got to beginning of file before newline
                break

    def end(self):
        """"""
        # move cursor to the last characters of the document, and then move
        # one more step to the last char '\n', which is exactly the `End`
        # position.

        # Each line's last character is also '\n'. But we'll not stop the
        # cursor there.

        # while (self.position < len(self.document.characters)) and \
        #        (self.document.characters[self.position] != '\n'):

        while self.position < len(self.document.characters) and \
              (self.document.characters[self.position].character != '\n'):
            self.position += 1


#############################################################################
class Character:
    """This class allows us to create characters and prefix them with a
    special character when the `str()` function is applied to them.

    This character object represents ONE rich text character.
    No matter how many characters is prefixed, the CORE character with
    the prefixes represent ONE position."""
    def __init__(self, character, bold=False, italic=False, underline=False):
        """"""
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        """Should `Character` even be a class, or a data structure with
        attributes?

        There is a very important special methodn on the `object` class
        that we can take advantage of to represent our characters.
        `__str__` is used in string manipulation function like `print`
        and the `str` constructor to covert any class to a string.

        We override it and we make it print whatever we like."""
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''

        return bold + italic + underline + self.character
