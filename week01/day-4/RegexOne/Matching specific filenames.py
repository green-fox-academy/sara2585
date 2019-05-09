import re
r = re.compile(r'(\w+)\.(png|jpg|gif)$')
print(r.match('.bash_profile'))
print(r.match('workspace.doc'))
print(r.match('updated_img0912.png').group(1,2))