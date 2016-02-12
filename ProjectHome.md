# JES 5.0 is in the works! #

The development of JES 5.0 has moved to GitHub. JES 4.3, which is the latest release version, still lives on this Web site. You can download it from:

> https://code.google.com/p/mediacomp-jes/downloads/list

But, if you want to help us with JES 5.0, or report issues, you should visit:

> https://github.com/gatech-csl/jes

## Welcome ##
This is the code repository for JES, the Jython Environment for Students.  It is an educational IDE used in the Media Computation curriculum developed by Mark Guzdial and Barbara Ericson at Georgia Tech.  More details on the curriculum are available at http://www.mediacomputation.org/.

Inside this Software Suite, you will find all the tools you need to make pictures, audio, and video using the Jython language.  Also included are, Barbara's Java mediacomp classes, previous releases of the software and JES.exe sources

JES releases are available under the Downloads tab on this site.  The current release version is 4.3, which makes use of 0-based media APIs.  If you need to use the older 1-based media APIs, you should use version 3.2.1.

Changes in 4.3
  * Windows versions now come with executable installers
  * Jython cache directory moved from program directories to temp storage to solve permission problems with installations on Windows Vista.
  * WriteAVI is back as an option for saving movies
  * Midi playback in Windows is fixed so that playNote(x) now functions
  * Misc minor bugfixes

Changes in 4.2.1
  * We have corrected a bug which caused writePictureTo to fail

Changes in 4.2/3.2
  * We have corrected a bug which intermittently resulted in JES hanging on pickAFile()
  * Functionality of input() and raw\_input() has changed to read input from the console instead of prompting for input via a dialog.
  * MediaPath now saves on close.
  * The program editor pane will now autoindent to the same indentation level as the previous line when enter is pressed
  * Help files improved and expanded to include all JES media functions
  * JES settings reworked internally
  * Removed turnin settings dialog an first launch
  * Centered JES and dialog windows on startup
  * Other minor bugfixes

Release Version SVN Information
  * [Revision 92](https://code.google.com/p/mediacomp-jes/source/detail?r=92) -- 4.3
  * [Revision 75](https://code.google.com/p/mediacomp-jes/source/detail?r=75) -- 4.2.1 / 3.2.1
  * [Revision 69](https://code.google.com/p/mediacomp-jes/source/detail?r=69) -- 4.2 / 3.2
  * [Revision 55](https://code.google.com/p/mediacomp-jes/source/detail?r=55) -- 4.2 (beta)