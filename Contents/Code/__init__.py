import os
from smi2srt import convertSMI

def Start():
  pass

def convertSubtitles(part, SaveSRT):
  Log(part.file)
  basePath = os.path.splitext(part.file)[0]
  smiPath = basePath+'.smi'
  if not os.path.exists(smiPath):
    return False

  ext = '.smi'

  # (1) transcode to CP949
  subData = Core.storage.load(smiPath)
  subEncoding = chdet(subData)
  
  # (2) convert SMI to SRT and save
  result = {'ko':''}
  if SaveSRT and subEncoding != 'Unknown':
    result['ko'] = convertSMI(subData.decode(subEncoding, 'ignore').encode('utf-8'))
    Log('convert(%s)' % (smiPath))
    ext = '.srt'
    Core.storage.save(basePath+'.ko'+ext, result['ko'])
    return True
  elif not SaveSRT:
      Log('SaveSRT false')

def chdet(aBuf):
    # If the data starts with BOM, we know it is UTF
  if aBuf[:3] == '\xEF\xBB\xBF':
    # EF BB BF  UTF-8 with BOM
    result = "UTF-8"
  elif aBuf[:2] == '\xFF\xFE':
    # FF FE  UTF-16, little endian BOM
    result = "UTF-16LE"
  elif aBuf[:2] == '\xFE\xFF':
    # FE FF  UTF-16, big endian BOM
    result = "UTF-16BE"
  elif aBuf[:4] == '\xFF\xFE\x00\x00':
    # FF FE 00 00  UTF-32, little-endian BOM
    result = "UTF-32LE"
  elif aBuf[:4] == '\x00\x00\xFE\xFF': 
    # 00 00 FE FF  UTF-32, big-endian BOM
    result = "UTF-32BE"
  elif aBuf[:4] == '\xFE\xFF\x00\x00':
    # FE FF 00 00  UCS-4, unusual octet order BOM (3412)
    result = "X-ISO-10646-UCS-4-3412"
  elif aBuf[:4] == '\x00\x00\xFF\xFE':
    # 00 00 FF FE  UCS-4, unusual octet order BOM (2143)
    result = "X-ISO-10646-UCS-4-2143"
  else:
    result = "Unknown"
  return result

# entry for Movie
class SmiSubtitleAgentMovies(Agent.Movies):
  name = 'SMI Converter'
  #languages = [Locale.Language.NoLanguage]
  languages = [Locale.Language.Korean]
  primary_provider = False
  
  def search(self, results, media, lang):
    results.Append(MetadataSearchResult(id = 'null', score = 100))
    
  def update(self, metadata, media, lang):
    SaveSRT = Prefs['save_srt']
    for i in media.items:
      for part in i.parts:
        convertSubtitles(part, SaveSRT)

# entry for TV shows
class SmiSubtitleAgentTV(Agent.TV_Shows):
  name = 'SMI Converter'
  #languages = [Locale.Language.NoLanguage]
  languages = [Locale.Language.Korean]
  primary_provider = False

  def search(self, results, media, lang):
    results.Append(MetadataSearchResult(id = 'null', score = 100))

  def update(self, metadata, media, lang):
    SaveSRT = Prefs['save_srt']
    for s in media.seasons:
      # just like in the Local Media Agent, if we have a date-based season skip for now.
      if int(s) < 1900:
        for e in media.seasons[s].episodes:
          for i in media.seasons[s].episodes[e].items:
            for part in i.parts:
              convertSubtitles(part, SaveSRT)