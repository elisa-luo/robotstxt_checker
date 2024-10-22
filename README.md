# robotstxt_checker
use the google robots.txt parser to check if a given user-agent is disallowed completely from a site

I provided the binary but it’s probs best to compile the google robots.txt parser on the machine you are running on. 
https://github.com/google/robotstxt

Basically we use the google robots.txt parser to check indivdual UAs and paths.
We enumerate through all paths provided in robots.txt.
