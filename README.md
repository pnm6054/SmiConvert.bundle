Convert subtitles in SMI to SRT
========================================

Plex agents to convert subtitles in SMI format to SRT format.

It demultiplex first if multiple language sections exist,
and then convert Korean section to SRT format.

TODO
-------------

* Support saving in ASS format
* Handling SMI file which has no language info header

--------------
Additional feature
* (Unicode with BOM, EUC-KR encoded)smi file convert to (utf-8 encoded)srt file

Acknowledge
-------------

* [smi2srt](https://gist.github.com/suapapa/1532257)
