# Python wrapper for Omxplayer (Raspberry Pi)

A dead simple wrapper of oxmplayer in python

```python

from pyomx import Pyomx
# args: [file path/url, audio out, loop, layout]
omxplayer = Pyomx('/path/to/video', 'hdmi', True, '2.1')
omxplayer.handle('pause');
omxplayer.handle('play');
omxplayer.handle('volume_up');
omxplayer.handle('volume_down');
omxplayer.handle('seek_rewind');
omxplayer.handle('seek_forward');
omxplayer.handle('stop');