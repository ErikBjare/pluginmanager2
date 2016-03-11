pluginmanager2
==============

Plugins are a vital part of many extensible applications and almost every program rolls their own despite many having similar requirements on their plugin systems. So, why not abstract it all away into a library and never rewrite another plugin system again? That's the purpose of this library.


## Goal
The goal of this project is to offer a generalized solution which can be used when a plugin system is needed in any Python program.

## Inspiration
 - [ZeroNet](https://github.com/HelloZeroNet/ZeroNet) (their [PluginManager](https://github.com/HelloZeroNet/ZeroNet/blob/master/src/Plugin/PluginManager.py))
 - [Deluge](http://deluge-torrent.org/) (their [PluginManager](http://git.deluge-torrent.org/deluge/tree/deluge/core/pluginmanager.py) and [PluginManagerBase](http://git.deluge-torrent.org/deluge/tree/deluge/pluginmanagerbase.py))

### Self-inspiration
This project was started since I desired a general solution to creating pluginmanagers which arose from my own need in the following projects:

 - [ActivityWatch](https://github.com/ErikBjare/activitywatch)
 - [Homebrain](https://github.com/Homebrain/Homebrain/) 

## Dependencies
No external dependencies. It's all pure Python, yay!

