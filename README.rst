.. image:: https://img.shields.io/pypi/v/beets.svg
    :target: https://pypi.python.org/pypi/beets

.. image:: https://img.shields.io/codecov/c/github/beetbox/beets.svg
    :target: https://codecov.io/github/beetbox/beets

.. image:: https://img.shields.io/github/actions/workflow/status/beetbox/beets/ci.yaml
    :target: https://github.com/beetbox/beets/actions

.. image:: https://repology.org/badge/tiny-repos/beets.svg
    :target: https://repology.org/project/beets/versions


beets
=====

Beets is the media library management system for obsessive music geeks.

The purpose of beets is to get your music collection right once and for all.
It catalogs your collection, automatically improving its metadata as it goes.
It then provides a bouquet of tools for manipulating and accessing your music.

Here's an example of beets' brainy tag corrector doing its thing::

  $ beet import ~/music/ladytron
  Tagging:
      Ladytron - Witching Hour
  (Similarity: 98.4%)
   * Last One Standing      -> The Last One Standing
   * Beauty                 -> Beauty*2
   * White Light Generation -> Whitelightgenerator
   * All the Way            -> All the Way...

Because beets is designed as a library, it can do almost anything you can
imagine for your music collection. Via `plugins`_, beets becomes a panacea:

- Fetch or calculate all the metadata you could possibly need: `album art`_,
  `lyrics`_, `genres`_, `tempos`_, `ReplayGain`_ levels, or `acoustic
  fingerprints`_.
- Get metadata from `MusicBrainz`_, `Discogs`_, and `Beatport`_. Or guess
  metadata using songs' filenames or their acoustic fingerprints.
- `Transcode audio`_ to any format you like.
- Check your library for `duplicate tracks and albums`_ or for `albums that
  are missing tracks`_.
- Clean up crufty tags left behind by other, less-awesome tools.
- Embed and extract album art from files' metadata.
- Browse your music library graphically through a Web browser and play it in any
  browser that supports `HTML5 Audio`_.
- Analyze music files' metadata from the command line.
- Listen to your library with a music player that speaks the `MPD`_ protocol
  and works with a staggering variety of interfaces.

If beets doesn't do what you want yet, `writing your own plugin`_ is
shockingly simple if you know a little Python.

.. _plugins: https://beets.readthedocs.org/page/plugins/
.. _MPD: https://www.musicpd.org/
.. _MusicBrainz music collection: https://musicbrainz.org/doc/Collections/
.. _writing your own plugin:
    https://beets.readthedocs.org/page/dev/plugins.html
.. _HTML5 Audio:
    https://html.spec.whatwg.org/multipage/media.html#the-audio-element
.. _albums that are missing tracks:
    https://beets.readthedocs.org/page/plugins/missing.html
.. _duplicate tracks and albums:
    https://beets.readthedocs.org/page/plugins/duplicates.html
.. _Transcode audio:
    https://beets.readthedocs.org/page/plugins/convert.html
.. _Discogs: https://www.discogs.com/
.. _acoustic fingerprints:
    https://beets.readthedocs.org/page/plugins/chroma.html
.. _ReplayGain: https://beets.readthedocs.org/page/plugins/replaygain.html
.. _tempos: https://beets.readthedocs.org/page/plugins/acousticbrainz.html
.. _genres: https://beets.readthedocs.org/page/plugins/lastgenre.html
.. _album art: https://beets.readthedocs.org/page/plugins/fetchart.html
.. _lyrics: https://beets.readthedocs.org/page/plugins/lyrics.html
.. _MusicBrainz: https://musicbrainz.org/
.. _Beatport: https://www.beatport.com

Install
-------

You can install beets by typing ``pip install beets`` or directly from Github (see details `here`_).
Beets has also been packaged in the `software repositories`_ of several
distributions. Check out the `Getting Started`_ guide for more information.

.. _here: https://beets.readthedocs.io/en/latest/faq.html#run-the-latest-source-version-of-beets
.. _Getting Started: https://beets.readthedocs.org/page/guides/main.html
.. _software repositories: https://repology.org/project/beets/versions

Contribute
----------

Thank you for considering contributing to ``beets``! Whether you're a
programmer or not, you should be able to find all the info you need at
`CONTRIBUTING.rst`_.

.. _CONTRIBUTING.rst: https://github.com/beetbox/beets/blob/master/CONTRIBUTING.rst

Read More
---------

Learn more about beets at `its Web site`_. Follow `@b33ts`_ on Mastodon for
news and updates.

.. _its Web site: https://beets.io/
.. _@b33ts: https://fosstodon.org/@beets

Contact
-------
* Encountered a bug you'd like to report? Check out our `issue tracker`_!
    * If your issue hasn't already been reported, please `open a new ticket`_
      and we'll be in touch with you shortly.
    * If you'd like to vote on a feature/bug, simply give a :+1: on issues
      you'd like to see prioritized over others.
* Need help/support, would like to start a discussion, have an idea for a new
  feature, or would just like to introduce yourself to the team? Check out
  `GitHub Discussions`_!

.. _GitHub Discussions: https://github.com/beetbox/beets/discussions
.. _issue tracker: https://github.com/beetbox/beets/issues
.. _open a new ticket: https://github.com/beetbox/beets/issues/new/choose

Authors
-------

Beets is by `Adrian Sampson`_ with a supporting cast of thousands.

.. _Adrian Sampson: https://www.cs.cornell.edu/~asampson/
