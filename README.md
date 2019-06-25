# Macos-Setup
自用！！！初始化mac的开发环境(Android、Flutter)

# 第一步
 去 <https://github.com/shadowsocks/ShadowsocksX-NG/releases> 准备好梯子
 
# 第二步
 安装 Xcode Command Line Tools
 
# 第三步 

```
 /usr/bin/python -c "$(curl -fsSL https://raw.githubusercontent.com/Wanchen7/Macos-Setup/master/macos-setup.py)"
```
# 第四步

* 安装oh-my-zsh 

	```
	sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
	```
* 安装plugins

	```
	brew install zsh-completions zsh-syntax-highlighting zsh-autosuggestions
	```
	
* 配置zshrc

	```
	sed -i -e \'s/robbyrussell/agnoster/g\' ~/.zshrc  &> /dev/null
	
	sed -i -e \'s/plugins=(git)/plugins=(git brew sublime zsh-autosuggestions zsh-syntax-highlighting)/g\' ~/.zshrc  &> /dev/null
	
	echo "DEFAULT_USER=\`whoami\`" >> ~/.zshrc
	
	echo "source ~/.bash_profile" >> ~/.zshrc
	```
* 配置iterm 
  <https://github.com/agnoster/agnoster-zsh-theme>
  