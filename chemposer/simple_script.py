from subprocess import call

ex = './chemposer'
filename = './static/xyz/tmp/C20.xyz'
call([ex, filename])
