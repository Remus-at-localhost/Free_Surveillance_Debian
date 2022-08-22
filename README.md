## Free_Surveillance
This Repository has all the files and scripts that will turn your laptop and spare phone into an efficient surveillance system.(As long as you want it to be ;D )

Why there are 2 Start files??
1.Start(Metasploit_Method) -> This is Method-1 and It uses Metasploit to get the reverse_tcp access of your phone and posts the captured images to discord server.
2.Start(Droicam_Method) -> This is Method-2 and It does the Exactly same thing! but needs the droid cam app on the phone.

Making a choice:
1.if your spare phone's OS is > Android 5.0 then you can use Both the methods
2.On the other hand if your phone is older, you can use the metasploit method.

## What you need for this?
1.A PC running (Linux) and a Spare Android Phone.
2.Python3 and make sure that Libraries [opencv,nunmpy,requests,pyautogui] are pre installed.
3.Tools required -> Metasploit and DroidCam.
4.Access_token and Group-ID of your Discord Server's text group.

##How to set this up?
1.Create a Discord Server and one text group within it, which will be dedicated thereafter for uploading the surveillance images.
2.Now make sure that you extract the [Access token] and [Group ID] of your Discord Server's text group.
  Need Help extracting these 2? watch this -> https://youtu.be/Qy6RiosHKo0
3.Once you have these 2 things, copy them to the [Token_Url_Id.txt] file.
4.For method-1, edit the changes in the Exploit.sh file [edit Listening Port and Listening Host]
5.For method-2, add the Droid cam url to the Token_Url_Id file. 


##How to use this?
1.Method-1 -> run the Start(Metaspoit_Method)
2.Method-2 -> run the Start(DroidCam_Method)
