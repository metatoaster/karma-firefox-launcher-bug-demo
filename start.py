import os
from subprocess import call

env = dict(os.environ)
base_env = {'PATH': env['PATH']}

def iter_env():
    for k in sorted(env.keys()):
        yield {k: env[k], 'PATH': env['PATH']}

args = ['node_modules/.bin/karma', 'start', 'karma.conf.js', '--color']
print('basic call')
rc = call(args, env=base_env)

for ie in iter_env():
    if rc == 1:
        break
    print('using env=%s' % ie)
    rc = call(args, env=ie)
