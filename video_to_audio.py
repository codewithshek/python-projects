# follow data._.pirates for more python contents
# Python code to convert video to audio 

import moviepy.editor as mp 

  
# Insert Local Video File Path  

clip = mp.VideoFileClip(r"Video File") 

  
# Insert Local Audio File Path 

clip.audio.write_audiofile(r"Audio File") 