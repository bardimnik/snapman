Snapman
-------

Snapman is a backup program based on the ability of Btrfs file system to
capture snapshots of subvolumes.

When you run `snapman` it will read its configuration file and then it will
make backups (snapshots) of indicated subvolumes at desired frequency until
reach a defined quota. If quota were reached, then it will remove the older
backup before to make a new one to keep the number of backups indicated in
quota.

Snapman will run periodically if you use the `--daemon` command line option.

Backups are stored in a directory specified in the configuration file.

For each subvolume that you want to backup you must to write at least an entry
in the configuration file (in the easy `.ini` format).

Snapman accepts command-line options to manage snapshots.

For futher details, read the included documentation:

- [INSTALL](INSTALL.html), for install instructions.

- [FAQ](FAQ.html), for Frequently Asked Questions.

- [NEWS](NEWS.html), for some news or changes in the application.

- [Snapman manual](man/en/snapman.1.md), for the manual.

- [Configuration manual](man/en/snapman.5.md), for the manual of configuration
    file syntax.

When the program is installed, all the documentation are available at
`/usr/share/doc/snapman`. And the manuals with:

        man snapman

And, for configuration file syntax:

        man 5 snapman
