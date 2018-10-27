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
+ (UCS-2 LE encoded)smi file convert
- (EUC-KR)smi file convert

Acknowledge
-------------

* [smi2srt](https://gist.github.com/suapapa/1532257)
