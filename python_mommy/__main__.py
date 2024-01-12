from . import *

fail = False
code = 1
try:
    code = subprocess.run(["python", *sys.argv[1:]]).returncode
except: fail = True
if locals().get('code', globals().get('code')) is None or code != 0: fail = True

situation = "negative" if fail else "positive"
print()
print(
    termcolor.colored(make_response(random.choice(responses[random.choice(MOMMYS_MOODS.split("/"))][situation])), attrs=["bold"])
)
exit(code)
