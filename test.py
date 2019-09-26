from subprocess import call, check_output
from optparse import OptionParser

def main():
    parser = OptionParser()
    parser.add_option('-c', '--command', dest='command', help='Add any command prompt or terminal command depending on the environment you are on')
    (option, args) = parser.parse_args()
    return option

def get_result(command):
    return str(check_output([command]))

def run_command(command):
    call([command])

command = main()
run_command(command.command)
result = get_result(command.command)

if result:
    list_result = result.split()
    for result in list_result:
        print(result)


