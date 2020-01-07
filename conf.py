# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/blog/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "ibaomu/blog@gh-pages"
}

# 站点设置
site_name = "wildtree"
site_logo = "${static_prefix}pink_sin.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "抱木"
email = "bkmu39@gmail.com"
author_homepage = "https://github.com/ibaomu"
description = "All those moments will be lost in time, like tears in rain."
key_words = ['blog', 'wildtree', 'growing', 'student']
language = 'zh-CN'
external_links = [
    {
        "name": "Home",
        "url": "https://github.com/ibaomu",
        "brief": "back to home"
    },
    {
        "name": "我的博客",
        "url": "https://github.com/ibaomu",
        "brief": "抱木的主页。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://github.com/ibaomu",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/ibaomu",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://github.com/ibaomu",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
