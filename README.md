#RobotRecorder
####Records NetworkTable values from robot and displays them on graphs for debuggin purposes

##Recorder
Running the recorder

~~~bash
./recorder.py
~~~

Options

- Verbose: `-v` or `verbose`
- IP: `-ip 127.0.0.1` localhost is defualt

##Reader
Running the reader

~~~bash
./reader.py
~~~

Options

- Files: `-f savefile.ntstore` or `--file savefile.ntstore` defaults to example
- Config: `-c config.json` or `--config config.json` defaults to example
- List: `-l` lists the keys in a ntstore file

###Configuration file

See `EaxampleConfig.json`