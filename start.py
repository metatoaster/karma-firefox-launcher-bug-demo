import os
from subprocess import call

env = dict(os.environ)
fail_env = {
    'PATH': env['PATH']
}

pass_env = {
    'PATH': env['PATH'],
    'HOME': env['HOME'],
}

args = ['node_modules/.bin/karma', 'start', 'karma.conf.js', '--color']

print('calling using just PATH defined: %s' % fail_env)
rc = call(args, env=fail_env)
print('exit status: %d' % rc)

print('calling using just PATH defined: %s' % pass_env)
rc = call(args, env=pass_env)
print('exit status: %d' % rc)
