---
title: "Qt without Xcode"
date: 2020-04-19T23:20:53+08:00
draft: false
tags: [Qt xcode]
categories: [Qt]
---
From https://gist.github.com/shoogle
================

***How to use Qt Creator for software development on macOS without having to install Xcode***

## Justification

Qt refuses to install on macOS unless Apple's Xcode is installed beforehand.
This is unfortunate because:

- __Xcode is huge!__
  - The full IDE is a 5 GB download, and can occupy 20 GB+ of space on disk.
- __Qt doesn't actually need the full IDE.__
  - Only Xcode's command line utilities are required for macOS application development¹.
- __Developers may never actually use Xcode.__
  - They can program in Qt Creator, like they do in Windows and Linux.

Downloading and installing the command line utilities *without* Xcode saves time and bandwidth,
and means that valuable SSD storage space is kept for better uses.

*¹ I believe the full Xcode IDE is required for developing iOS apps with Qt
(i.e. apps for iPads and iPhones)
but I'm not sure about this as I'm not an iOS developer.*

## Instructions

### Summary

1. __Install Xcode's Command Line Tools (i.e. not Xcode itself).__
  - Run in Terminal: `xcode-select --install`
2. __Install Qt using the Online Installer.__
  - Download links:
    - Open Source: <https://www.qt.io/download-open-source>
    - Commercial: <https://www.qt.io/download>
  - The installer will complain that Xcode is not installed.
    - Keep clicking "OK" until the message goes away permanently (after 12 clicks).
  - Remember where you installed Qt (default location is `~/Qt`).
    - If you used a different location then you will need to change subsequent commands accordingly.
3. __Make sure Qt Creator uses the correct C++ Compiler.__
  - Launch Qt Creator for the first time from the command line,
  with the location of the command line tools compilers in `${PATH}`:
    - `PATH="$(xcode-select -p)/usr/bin:${PATH}" ~/Qt/Qt\ Creator.app/Contents/MacOS/Qt\ Creator`
  - Go to Qt Creator > Preferences > Build & Run > Kits and select a build kit (e.g. `Desktop Qt 5...`).
  - Check that both the C compiler and the C++ compiler are:
    - `clang` (not `gcc`)
    - from the Command Line Tools (not the default compilers in `/usr/bin`)
  - Close Qt Creator.
    - You can launch Qt Creator the normal way in future (e.g. via Spotlight).
4. __If your Qt version is older than Qt 5.9.2 then you need to update some QMake files.__
  - Navigate to the directory `~/Qt/<version>/clang_64/mkspecs/features/mac`
  - Make a backup copy of the following files before replacing them with newer versions from [this git commit][commit-diff]:
    - Replace `sdk.prf` with this [newer version][sdk.prf].
    - Replace `default_pre.prf` with this [newer version][default_pre.prf].
    - Make this change to the file `default_post.prf`:
      - Find the line `cache(QMAKE_XCODE_VERSION, stash)`
      - Replace it with `!isEmpty(QMAKE_XCODE_VERSION): cache(QMAKE_XCODE_VERSION, stash)`

All done!

[commit-diff]: https://github.com/qt/qtbase/commit/fa7626713b3a943609453459190e16c49d61dfd3 "git commit diff"
[sdk.prf]: https://github.com/qt/qtbase/blob/fa7626713b3a943609453459190e16c49d61dfd3/mkspecs/features/mac/sdk.prf
[default_pre.prf]: https://github.com/qt/qtbase/blob/fa7626713b3a943609453459190e16c49d61dfd3/mkspecs/features/mac/default_pre.prf

## Step-by-step

### Step 1 - Download & install Xcode's Command Line Tools

Open a Terminal (press Cmd+Space and type "Terminal") and enter this command:

  ```bash
  xcode-select --install
  ```

Press the Return key to execute the command.

### Step 2 - Download & install Qt and Qt Creator

Packages are available for MacPorts and Homebrew,
but it's usually best to get it straight from the source:

- Open Source: <https://www.qt.io/download-open-source>
- Commercial: <https://www.qt.io/download>

The Online Installer is probably the best option for most people.

*Tip: when you run the Online Installer it will prompt you to log in with Qt online credentials,
but open-source users can skip this step without entering anything.*

At a certain point during the install the following error message will appear:

> You need to install Xcode version 5.0.0.
> Download Xcode from https://developer.apple.com/xcode

Press "OK" or ESC to dismiss the dialog. It will come back again.
**Keep pressing "OK" or ESC and the dialog will eventually go away for good!**
You have to dismiss the dialog a total of 12 times before you can continue.

*Hint: Once Qt is installed you can delete the installer as you won't need it again.
If you want to update or remove Qt you have to use the MaintenanceTool in the Qt directory.*

### Step 3 - Make sure Qt Creator uses the correct C++ Compiler.

Run this command in a Terminal windows to find out where Xcode's Command Line Tools are installed:

  ```bash
  xcode-select --print-path
  ```

The result will probably be `/Library/Developer/CommandLineTools`,
unless Xcode is installed. Whatever the result,
you need to append "/usr/bin" to get something along the lines of:

  ```bash
  /Library/Developer/CommandLineTools/usr/bin
  ```

Run Qt Creator once with this location stored in your `${PATH}` environment variable:

  ```bash
  PATH="$(xcode-select -p)/usr/bin:${PATH}" ~/Qt/Qt\ Creator.app/Contents/MacOS/Qt\ Creator
  ```

Go to Qt Creator > Preferences > Build & Run > Kits and select a build kit (e.g. `Desktop Qt 5...`).

Check that the C and C++ compilers are the ones from the command line tools,
not the default compilers in `/usr/bin`.
Also check that `clang` is used for both compilers, not `gcc`.

Qt Creator will remember the locations of the compilers,
so in future you can launch Qt Creator the normal way via Spotlight.

### Step 4 - Update some QMake files (only necessary for Qt versions older than Qt 5.9.2)

The `xcrun` or `xcodebuild` utilities can be used to show where Xcode's Command Line Tools are installed,
but only `xcrun` works when Xcode itself is not installed.

#### Qt 5.9.2 and later

Recent Qt versions use `xcrun` already, so there's nothing left for you to do!

#### Qt 5.9.1 and older

Older Qt versions try to use `xcodebuild` to find out where the utilities are installed.
This fails with the following error message unless Xcode is installed:

> Project ERROR: Could not resolve SDK Path for 'macosx'
> Error while parsing file `<filename.pro>`. Giving up.

You need to tell QMake to use `xcrun` instead.

Open a Terminal and change directory to where the QMake files are stored.

  ```bash
  cd ~/Qt # or wherever you installed Qt
  cd 5.8 # or whichever version you have installed
  cd clang_64/mkspecs/features/mac
  ```

Now copy and paste these new commands __into the same Terminal window__
to create backup copies of some files:

  ```bash
  function backup_files() {
    for file in "$@"; do
      [[ -f "${file}.backup" ]] || cp "${file}" "${file}.backup"
    done
  }
  backup_files sdk.prf default_pre.prf default_post.prf
  ```
Press the Return key after the final command.

If that all went OK then run these commands to update the files:

  ```bash
  url_base='https://raw.githubusercontent.com/qt/qtbase'
  commit='fa7626713b3a943609453459190e16c49d61dfd3'
  dir='mkspecs/features/mac'
  curl -O "${url_base}/${commit}/${dir}/sdk.prf"
  curl -O "${url_base}/${commit}/${dir}/default_pre.prf"
  old_line='cache(QMAKE_XCODE_VERSION, stash)'
  new_line='!isEmpty(QMAKE_XCODE_VERSION): cache(QMAKE_XCODE_VERSION, stash)'
  sed "s|^${old_line}\$|${new_line}|" <default_post.prf.backup >default_post.prf
  ```

You can see the changes made [here][commit-diff] if you are interested.

## Reusing this material

### Referencing

[Qt without Xcode how-to][gist] by Peter Jonas ([shoogle]) / [CC BY 4.0][CC-BY]

[gist]: https://gist.github.com/shoogle/750a330c851bd1a924dfe1346b0b4a08 "GitHub gist"
[shoogle]: https://github.com/shoogle "shoogle's GitHub user profile"

### License

[![Creative Commons License][CC-BY-image]][CC-BY]

This work is licensed under a [Creative Commons Attribution 4.0 International License][CC-BY].

[CC-BY]: http://creativecommons.org/licenses/by/4.0/ "View license text on the Creative Commons website"
[CC-BY-image]: https://i.creativecommons.org/l/by/4.0/88x31.png "CC BY"
