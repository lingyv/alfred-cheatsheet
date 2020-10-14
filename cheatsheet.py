#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'lingyv'


import sys
import os
from workflow import Workflow3, ICON_WARNING

def main(wf):
    query = None
    if len(wf.args):
        query = wf.args[0]
    items = os.listdir('./cheatsheet')
    if query and len(query.split(" ")) > 1:
        all_lines = []
        ql = query.split(" ")
        for f in items:
            if ql[0]==f:
                with open("./cheatsheet/{}".format(f), 'r') as f:
                    for line in f.readlines():
                        all_lines.append(line.decode('utf-8').strip('\n'))
        items = all_lines
        query = ql[1]
    items = wf.filter(query, items)
    if not items:
        wf.add_item('未查找到相关内容', icon=ICON_WARNING)
    else:
        for item in items:
            wf.add_item(item, query, arg=item, valid=True, autocomplete=item)
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))