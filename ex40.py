class Song(object):
 def __init__(self, lyrics):
  self.lyrics = lyrics
 
 def sing_me_a_song(self):
  for line in self.lyrics:
   print line
   
class Song2(Song):
 def __init__(self, lyrics):
  self.lyrics = lyrics
  self.lyrics = ' '.join(self.lyrics) 
   
happy_bday = Song(["Happy birthday to you", 
 "I don't want to get sund",
 "So I 'll stop right there"])  
 
bulls_on_parade = Song(["They rally around the family",
 "With pockets full of shells"])
 
i_love_you = Song2(["I love you so much",
 "I wrote a song for you",
 "In my python codes",
 "my dear Yun"])
 
 
 
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

i_love_you.sing_me_a_song()
