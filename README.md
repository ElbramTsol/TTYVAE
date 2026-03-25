# TTYVAE
A script using Python, Selenium, &amp; Undetected_Chromedriver to automatically export twitch VODs to Youtube, because Twitch refuses to offer this option.

Here is a quick expose of what's going to happen when you run the spoopy file that has been delivered unto your computer, from the web, at your behest & how to set it up.
This, is not a virus, I promise.
If you learn to code, you can fact check that.

#1 Assuming you have all required libraries, a chromium window will open to a Twitch sign in page, sign in however you do normally.
#2 There may or may not be a Google sign in page, as twitch has recently changed how exporting works, sign in however you do normally if it appears.
#3 The script will take the most recent VOD from your twitch channel, & automatically export it to a youtube channel.

After it is run for the first time, you will not need to repeat step one & two as long as the Twitch & Google izzat (cred (credentials)) remain valid, reducing flow to this.

#1 The script will take the most recent VOD from your twitch channel, & automatically export it to a youtube channel.

If you want this process to repeat, I recommend using your OS to schedule a task where the script is run.
You should also know that twitch does save defaults for exports, so you can turn off the config file almost entirely.

To the twitch devs I ask, was that so hard?

Required libraries: selenium & Undetected_Chromedriver.
Required software: Chromium
Because a webdriver is not a browser but manipulates a pre-existing one.

Now, for some slightly more technical documention.

Session tokens are no longer saved in local storage.json & session_tokens.pkl, being un-used. I am sure it could be implemented to take tokens from an existing browser & inject them into chrome removing the need to sign in even once, but the script does everything I want it to now, so I bequeeth it's undertaking unto the community.
If that were done, the entire selenium profile folder generated from using a saved profile could be eliminated, but, session_tokens.pkl & local_storage.json would need to be deleted for privacy.

That is all, the documentation I think is required. I have never started an opensource project before, but feel free to do with it as you please, so long as this project, me, & it's contributers, however few, are credited.
