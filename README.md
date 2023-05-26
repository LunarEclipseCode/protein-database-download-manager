## RCSB Protein Database Download Manager

This program batch downloads 3d model of proteins in pdb format
from the [Worldwide Protein Data Bank](https://ftp.wwpdb.org/pub/pdb/data/structures/divided/pdb/) . You can open pdb files using softwares like [Jmol](https://jmol.sourceforge.net/) or [PyMOL](https://pymol.org/) . Note that RCSB has it's own batch downloading feature too. You can check it out [here](https://www.rcsb.org/downloads). If you have a list of random pdb files you want to download, then RCSB's batch download is the way to go. If you want to download 'sequentially', for example, all pdb files under folder v5 to vq. Then this script is for you.

The database updates every week and the program can be used to check what new proteins from the database in missing on your computer, and download those files. 

If you look into the database, you will figure out the naming pattern of the files. Let's say you want to download all pdb files under folder v5 to vq. Then, set `alphabet` to 'v', `start` to '5' and `end` to 9. That's all you have to do. If the folder doesn't exist, the code will also create the folder for you. When you run the script for the first time, it will just download all pdb files under folder v5 to vq. Now if you run this script with those same variables six months later, the code will check what new files have been added to the database and only download those. 


