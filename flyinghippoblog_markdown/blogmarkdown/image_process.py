#coding=utf-8
import os
import argparse


path_offline = r"F:\flyinghippoblog_markdown\blogimage" + '\\' 
path_online = "https://raw.githubusercontent.com/flyinghippof/blogimage/master/"

path_out = 'changes/'
if not os.path.exists(path_out):
    os.mkdir(path_out)

ap = argparse.ArgumentParser()
ap.add_argument("-p","--path",default="original\\test.md",help="the path of your md file")

if __name__ == '__main__':
    args = ap.parse_args()
    path_md = args.path


    if '\\' in path_md:
        folder, name = path_md.split('\\')
    else:
        name = path_md
    path_out_md = "changes\\" + name
    print("markdown_online", path_out_md)

    with open(path_md, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    out = [l.replace(path_offline, path_online) for l in lines]

    with open(path_out_md, 'w', encoding='utf-8') as f:
        f.writelines(out)