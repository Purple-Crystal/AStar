string="Congrats on solving the first level of this task! You were able to figure out the ASCII text from the image, but wait! Your journey is not yet over. After the end of the text you will find a (200, 150, 3) coloured image. This image is a part of the bigger image called 'zucky_elon.png'. Find the top left coordinate (Image convention) from where this image was taken. The x coordinate represents the colour of a monochrome maze hidden in an image with coloured noise. Find the maze and solve the maze using any algothrim like dfs but better. Try comparing them and seeing how they perform like A*, RRT, RRT* for example. Once the maze is solved you will see a word. This word is a password to a password protected zip file which contains a png. Note that the password is case sensitive and all the aplhabets in the password will be capital letters This is your treasure. To open the treasure you need to convert the image in to an audio file in a simple way like you did for this ASCII text. Once converted, open the .mp3 file and enjoy your treasure, you deserved it! A part of the image 'zucky_elon.png' will begin immediately after the colon,image-IV2:"
count = 0;  
#Counts each character
for i in range(0, len(string)):  
  count = count + 1;  
   
#Displays the total number of characters present in the given string  
print("Total number of characters in a string: " + str(count));  