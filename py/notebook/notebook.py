#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

# Store the next available id for all new notes

__all__ =['Note', 'Notebook']

last_id = 0

class Note:
    """Represent a note in a notebook.  Match against a string in searches
and store tags for each note."""

    def __init__(self, memo, tags=''):
        """Initialize a note with memo and optional space-separated tags.
Automatically set the note's creation data and a unique id."""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, note_filter):
        """Determine if this note matches the fileter text.  Return True if it
matches, False otherwise.

        Search is case sensitive and matches both text and tags."""
        return (note_filter in self.memo) or (note_filter in self.tags)


class Notebook:
    """Represent a collection of notes that can be tagged, modified, and
searched."""
    def __init__(self):
        """Initialize a notebook with an empty list."""
        self.notes = []

    def new_note(self, memo, tags=''):
        """Create a new note and add it to the list."""
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        """Find the note with the given id and change its memo to the given
value."""
        # version 0.1
        # for note in self.notes:
        #     if note.id == note_id:
        #         note.memo = memo
        #         break

        # version 0.2
        #  self._find_note(note_id).memo = memo

        # version 0.3
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        """Find the note with the given id and change its tags to the given
value."""
        # v0.1
        # for note in self.notes:
        #     if note.id == note_id:
        #         note.tags = tags
        #         break

        # v 0.2
        # self._find_note(note_id).tags = tags

        # v0.3
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False

    def search(self, note_filter):
        """Find all notes that match the given filter string."""
        return [note for note in self.notes if note.match(note_filter)]

    #  There are duplicate codes in modify_memo and
    #  modify_tags. That't not a good practice.  Let's improve it.  Do
    #  it once, and once only.
    def _find_note(self, note_id):
        # Tips: the underscore indicates this method is intended to be
        # private.
        """Locate the note with the given id."""
        for note in self.notes:
            # if note.id == note_id:
            if str(note.id) == str(note_id):
                return note
        return None  # If no note is found, return None.


if __name__ == "__main__":
    pass

# from notebook import Note, Notebook
# >>> n = Notebook()
# >>> n.new_note("Hello, world!")
# >>> n.new_note("Hello, again")
# >>> n.notes
# [<notebook.Note object at 0x7f56df800080>, <notebook.Note object at 0x7f56df8000f0>]
# >>> n.notes[1].id
# 2
# >>> n.notes[0].id
# 1
# >>> n.notes[0].memo
# 'Hello, world!'
# >>> n.search("Hello")
# [<notebook.Note object at 0x7f56df800080>, <notebook.Note object at 0x7f56df8000f0>]
# >>> n.search("again")
# [<notebook.Note object at 0x7f56df8000f0>]
# >>> n.modify_memo(1, "Hi, world!")
# >>> n.notes[0].memo
# 'Hi, world!'
