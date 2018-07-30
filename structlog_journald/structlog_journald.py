# -*- coding: utf-8 -*-

"""Main module."""

import systemd.journal as journal


class JournalLoggerFactory(object):
    """
    Produce :class:`JournalLogger`\ s.

    To be used with :func:`structlog.configure`\ 's `logger_factory`.

    Positional arguments are silently ignored.

    """

    def __call__(self, *args):
        return JournalLogger()


class JournalLogger(object):
    """
    Write events into the systemd journal.

    >>> from structlog import JournalLogger
    >>> JournalLogger().msg("hello")
    # In journalctl -> hello

    """

    def __repr__(self):
        return "<JournalLogger>"

    def msg(self, message, *args, **kwargs):
        """
        Log *message* into the journal.
        """
        journal.send(message)

    log = debug = info = warn = warning = msg
    failure = err = error = critical = exception = msg
