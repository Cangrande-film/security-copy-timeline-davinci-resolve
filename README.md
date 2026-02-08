This is a quick script to create security copies of your current timeline in DaVinci Resolve. 
It quickly duplicates the timeline in the same bin with the date and time as a suffix to the timeline name, to make them easily distinguishable and organizable.
Also, Resolve doesn't switch to the new security timeline, making the process of making a duplicate less of an interruption.

In order to make use of this script, copy and paste the script in the following folders depending on your OS,

Windows:

  All users:

      %PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Fusion\Scripts
       
  Specific user:
  
       %APPDATA%\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts

Mac:

  All users:

       /Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts
       
  Specific user:
  
       /Users/<UserName>/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts

Linux:

  All users:

        /opt/resolve/Fusion/Scripts
        
  or

	      /home/resolve/Fusion/Scripts/
       
  Specific user:
  
       $HOME/.local/share/DaVinciResolve/Fusion/Scripts

After this, you should be able to run your script from Workspace -> Scripts
