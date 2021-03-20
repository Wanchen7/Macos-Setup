#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import os

# 检查 Xcode Command Line Tools 
if os.system('xcode-select -p') != 0:
  os.system('xcode-select --install')
  print "**************************************************************"
  print "请先安装 XCode Command Line Tools"
  print "**************************************************************"
  exit()


# 安装 HomeBrew
print "安装 HomeBrew"
os.system('cd ~ && curl -O https://raw.githubusercontent.com/Wanchen7/Macos-Setup/master/.bash_profile')
os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
os.system('brew tap caskroom/cask')
os.system('brew tap homebrew/services')
os.system('brew tap caskroom/versions')
os.system('brew tap caskroom/fonts')
os.system('brew update && brew upgrade && brew cleanup && brew cask cleanup')

# 安装 语言环境
print "安装 Git+Dart+Python"
os.system('brew install git dart python python3')
os.system('brew link --overwrite git dart python python3')
os.system('brew unlink python && brew link --overwrite python') # Fixes an issue with pip
os.system('brew install git-flow git-lfs')
os.system('git lfs install')


# 安装 第三方库
print "安装 第三方库"
os.system('brew install expect curl wget sqlite libpng libxml2 openssl unzip apktool dex2jar gradle')

# 安装 字体
print "安装 字体"
os.system('brew install --cask font-dosis font-droid-sans-mono-for-powerline font-open-sans font-open-sans-condensed font-roboto font-roboto-mono font-roboto-condensed font-roboto-slab font-consolas-for-powerline font-dejavu-sans font-dejavu-sans-mono-for-powerline font-inconsolata font-inconsolata-for-powerline font-lato font-menlo-for-powerline font-meslo-lg font-meslo-for-powerline font-noto-sans font-noto-serif font-source-sans-pro font-source-serif-pro font-ubuntu font-pt-mono font-pt-sans font-pt-serif font-fira-mono font-fira-mono-for-powerline font-fira-code font-fira-sans font-source-code-pro')

#系统设置
os.system('defaults write com.apple.finder AppleShowAllFiles -bool true')

# 安装 Android+Java环境
print "安装 Android+Java环境"
show_notification("请输入密码")
os.system('brew install --cask java8')
os.system('brew install --cask android-studio')
os.system('brew install android-platform-tools')

# 安装 Flutter环境
print "安装 Flutter环境"
os.system('cd ~/Documents && git clone -b master https://github.com/flutter/flutter.git && cd ~')

# 安装 Quicklook
print "安装 Quicklook"
os.system('brew install --cask qlcolorcode qlmarkdown quicklook-csv quicklook-json webpquicklook suspicious-package epubquicklook qlstephen qlprettypatch font-hack qlvideo')

# 安装 Vim
print "安装 vim"
os.system('brew install vim --with-override-system-vi')
os.system('git clone https://github.com/amix/vimrc.git ~/.vim_runtime')
os.system('sh ~/.vim_runtime/install_awesome_vimrc.sh')

# 安装 App
print "安装 app"
os.system('brew install --cask iterm3 wechat google-chrome sourcetree sublime-text wireshark qq macdown charles alfred postman android-file-transfer jd-gui karabiner-elements diffmerge')


