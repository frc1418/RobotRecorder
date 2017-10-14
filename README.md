# RobotRecorder
Records NetworkTables values and displays them on graphs for debugging.
![Screenshot](ss.png)

## Recording data
```sh
./recorder.py
```
This script will grab all NetworkTables values on the provided IP. These values will be stored on disconnect from server to be accessed later by the reader from `saves/`. Live NT data will also be shown when connected to a server.

**WARNING:** Do not exit the recorder until disconnected from the server. Data **WILL NOT** be stored.

Options:
- IP: `--ip 127.0.0.1`
- Verbose: `-v` or `verbose`
- Config: `-c filename` or `--config filename`. Defaults to `config.json`.

## Reading data
```sh
./reader.py
```
This script will allow viewing of saved data.

Options:
- File: `-f savefile.ntstore` or `--file savefile.ntstore`.
- Config: `-c filename` or `--config filename`. Defaults to `config.json`.
- List: `-l` lists the keys in an ntstore file.

## Configuration
Configuration is done through a JSON-formatted file. An example of one configuration can be found in `config.json.example`. You may rename this file and edit it to suit your needs.

## Samples
Some example data gathered by [FRC Team 1418](https://github.com/frc1418) can be found in `saves/examples/`.

## Authorship & Licensing
This software was created by [Carter Fendley](https://github.com/CarterFendley). [Erik Boesen](https://github.com/ErikBoesen) has also made contributions.

RobotRecorder is offered under the [MIT License](LICENSE).
