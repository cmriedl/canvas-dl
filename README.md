canvas-dl
=========
Download videos embedded into Canvas because *freedom*.

Usage
-----
 - navigate to the actual website with the embedded video in Canvas in a browser
   (note: all other videos in that module will also be downloaded)
 - save page (in FF this is `Web Page, complete`) - should download an `.html` file and
   an actual `files` directory (we want the `files` directory)
 - run (note: single quotes): `./canvas-dl.sh '<path to downloaded files directory>'`
 - patience
 - more patience
 - videos are downloaded into: `canvas-dl/module_<n>/` subdirectories
