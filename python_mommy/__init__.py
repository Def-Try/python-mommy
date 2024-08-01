import random
import subprocess
import sys
import colorama
import termcolor
import os
import signal

from . import responses

# config. separate with "/" to make a list of choices
MOMMYS_ROLE = os.environ.get("PYTHON_MOMMYS_ROLE", "mommy") # anything
MOMMYS_PRONOUNS = os.environ.get("PYTHON_MOMMYS_PRONOUNS", "her") # anything
MOMMYS_LITTLE = os.environ.get("PYTHON_MOMMYS_LITTLE", "girl") # anything
MOMMYS_EMOTES = os.environ.get("PYTHON_MOMMYS_EMOTES", "❤️/💖/💗/💓/💞") # anything
MOMMYS_MOODS = os.environ.get("PYTHON_MOMMYS_MOODS", "chill") # strictly chill/thirsty/yikes
MOMMYS_PARTS = os.environ.get("PYTHON_MOMMYS_PARTS", "milk") # anything
MOMMYS_FUCKING = os.environ.get("PYTHON_MOMMYS_FUCKING", "slut/toy/pet/pervert/whore") # anything
MOMMYS_PYTHON = os.environ.get("PYTHON_MOMMYS_INTERPRETER", "python3/python/py") # an interpreter(s) to try

colorama.just_fix_windows_console()

for mood in MOMMYS_MOODS.split("/"):
    if mood not in responses.keys():
        print(termcolor.colored("mommy does not like her mood \""+mood+"\"~"))
        exit(1)

def make_response(template):
    return template.replace("MOMMYS_ROLE", random.choice(MOMMYS_ROLE.split("/")))\
                   .replace("AFFECTIONATE_TERM", random.choice(MOMMYS_LITTLE.split("/")))\
                   .replace("DENIGRATING_TERM", random.choice(MOMMYS_FUCKING.split("/")))\
                   .replace("MOMMYS_PRONOUN", random.choice(MOMMYS_PRONOUNS.split("/")))\
                   .replace("MOMMYS_PART", random.choice(MOMMYS_PARTS.split("/")))\
                   + " " + random.choice(MOMMYS_EMOTES.split("/"))

def main():
    fail = False
    code = 1

    proc = None

    def resend_sig(signum, frame):
        # proc.send_signal(signum) # We don't need to do that as inner python already gets same signal
        pass

    catchable_sigs = set(signal.Signals) - {signal.SIGKILL, signal.SIGSTOP}
    # Make sure that we still can be stopped by SIGKILL and SIGSTOP
    for sig in catchable_sigs:
        signal.signal(sig, resend_sig)

    # try to find suitable interpreter from PYTHON_MOMMY_INTERPRETERS
    interpreter = "python"
    for intp in MOMMYS_PYTHON.split("/"):
        try:
            proc = subprocess.run([intp, '-c', '"exit()"'])
            if proc.returncode == 0:
                interpreter = intp
                break
        except: pass

    # actually run interpreter
    code = 1
    try:
        proc = subprocess.run([interpreter, *sys.argv[1:]])
        code = proc.returncode
    except: fail = True
    if code != 0: fail = True

    # select whether our situation is positive (code is 0) or negative (code != 0 or exception)
    situation = "negative" if fail else "positive"
    print()
    print(
        termcolor.colored(make_response(random.choice(responses[random.choice(MOMMYS_MOODS.split("/"))][situation])), attrs=["bold"])
    )
    exit(code)

if __name__ == "__main__":
    main()
