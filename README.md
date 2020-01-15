# boxToPlexSync

## Description
**EDIT**: This is the first Python program I ever wrote publicly and obviously it wasn't of high quality. There should have been classes defined which I didn't even know about when I was learning Python at this point. I didn't complete it either because my Box account was managed by my university so I couldn't get more than a 1 hour development token; therefore, it was never worth me refactoring and continuing to improve. I'm leaving this here as archived to show that it's okay to not be great at something, especially starting out. You're not ever expected to be an expert when learning something new. It's okay to make mistakes, do something wrong, and not have the best solution the first time. That's how you learn. I'm proud to say that this was one of my first forays into Python.

A Python program that merges the contents of a Box Sync folder online with a local folder. Box Sync does not have a Linux client. I wanted to sync the contents of a box folder containing media with a Plex Server running on a Raspberry Pi. The program requires ```cron``` to schedule the file to be run every hour or however often you want it to update.

This program is tested; however, not extensively and could not be deployed for my account because I do not have admin priveleges on my Box account (it is through my college). 
