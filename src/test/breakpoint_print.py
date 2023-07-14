from util import *
import re

send_gdb('b main')
expect_gdb('Breakpoint 1')

send_gdb('commands 1')
send_gdb('print 123 + 456')
send_gdb('end')

send_gdb('c')
expect_gdb('Breakpoint 1')
expect_gdb('579')

ok()
