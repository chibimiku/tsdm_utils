@ECHO OFF
SET /a _rand=(%RANDOM%*500/32768)+1
ECHO Random number %_rand% 