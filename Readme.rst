mdx-journal
===========

Extend Python Markdown with the `gthnk <http://gthnk.com>`_ journal annotation format.  With this extension installed, all datestamps and timestamps will be rendered as headings.

Installation
------------

    pip install mdx-journal

An example
----------

First, let's look at a journal entry without this custom markup.

::

    >>> from markdown import markdown
    >>> text = "2013-12-16\n\n1620\n\nThis is the first entry\n1621\n\nAnd this is the second entry"
    >>> markdown(text)
    u'<p>2013-12-16</p>\n<p>1620</p>\n<p>This is the first entry\n1621</p>\n<p>And this is the second entry</p>'

Now let's look at a journal entry with journal markup applied.  You will see that dates and times are now wrapped in heading tags.

::

    >>> markdown(text, extensions=["journal"])
    u'<p><h3>2013-12-16</h3></p>\n<p><h4>1620</h4></p>\n<p>This is the first entry\n<h4>1621</h4></p>\n<p>And this is the second entry</p>'

License
-------

MIT License.
