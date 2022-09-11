## Free_Surveillance
This Repository has all the files and scripts which creates an efficient surveillance system from using
1.PC(Any Debian based, in my case I have used Kali)
2.Spare mobile(Android)
3.Discord Server dedicated for controling & monitoring the surveillance system.


Why there are 2 Start files??
1.Start(Metasploit_Method) -> This is Method-1 and It uses Metasploit to get the reverse_tcp access of your phone and posts the captured images to discord server.
2.Start(Droicam_Method) -> This is Method-2 and It does the Exactly same thing! but needs the droid cam app installed on the phone.


Making a choice:
1.If your spare phone's OS is > Android 5.0 then you can use Both the methods.
2.On the other hand if your phone is older,then use the metasploit method.

## What you need for this?
1.A PC running (Linux) and a Spare Android Phone.
2.Python3 and make sure that Libraries [opencv,nunmpy,requests,pyautogui] are installed.
3.Tools required -> Metasploit and DroidCam (depending on the method you want to use).
4.Access_token and Group-ID of your Discord Server's text group ["CONFIDENTIAL CREDENTIALS, DON'T SHARE IT WITH ANYBODY!!"].

##How to set this up?
1.Create a Discord Server and one text group within it, which will be dedicated thereafter for uploading the surveillance images and controlling the system through user-defined commands.
2.Now make sure that you extract the [Access token] and [Group ID] of your Discord Server's text group.
  Need Help extracting these 2? watch this -> https://youtu.be/Qy6RiosHKo0
3.Once you have these 2 things, copy them to the [Token_Url_Id.txt] file.
4.For method-1, edit the changes in the Exploit.sh file [edit Listening Port and Listening Host] after setting up the reverse tcp access.
5.For method-2,Install Droid cam on your spare mobile and add the generated Droid cam url to the Token_Url_Id file. 


##How to use this?
1.Method-1 -> run the Start(Metaspoit_Method)
2.Method-2 -> run the Start(DroidCam_Method)


