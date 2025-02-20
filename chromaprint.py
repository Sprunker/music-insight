import essentia
from essentia.standard import MonoLoader, Chromaprinter
import urllib.request

class ChromaprintExtractor:
    def __init__(self):
        self.client_key = "HmgJ1ITJCf"

    def get_chromaprint(self, audio_file):
        """Calculate the Chromaprint for the given audio file and return the fingerprint and duration."""

        audio = MonoLoader(filename=audio_file, sampleRate=44100)()
        
        fingerprint = Chromaprinter()(audio)
        duration = len(audio) / 44100.

        return fingerprint, duration

    def query_acoustid(self, audio_file):
        """Query the AcoustID API using the Chromaprint."""
        fingerprint, duration = self.get_chromaprint(audio_file)

        query = f'http://api.acoustid.org/v2/lookup?client={self.client_key}&meta=recordings+releasegroups+compress&duration={int(duration)}&fingerprint={fingerprint}'
        
        with urllib.request.urlopen(query) as page:
            response = page.read()
        
        return fingerprint, response