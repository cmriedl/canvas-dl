canvas-dl
=========
Download videos embedded into Canvas because *freedom*.

Usage
-----
 - navigate to the actual website with the embedded video in Canvas in a browser
   (note: all other videos in that module will also be downloaded)
 - copy the URL of the iframe housing the embedded player.
   (note: in firefox, right click within the frame and select 'This Frame > View
   Frame Info', then copy the value of 'Address' in the General info pane.)
 - run (note: single quotes): `./canvas-dl.sh '<url address of embedded player frame>'`
 - patience
 - more patience
 - videos are downloaded into: `canvas-dl/module_<n>/` subdirectories
