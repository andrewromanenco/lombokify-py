# Lombokify
This is not a full program. This is an experiment of using ANTLR in python3. The goal is to implement a simple java 8 parser with extensibility to add AST processing logic.

## Usage notes
Install ANTLRer using steps from: https://www.antlr.org
```
cd /usr/local/lib
sudo curl -O https://www.antlr.org/download/antlr-4.9.2-complete.jar
export CLASSPATH=".:/usr/local/lib/antlr-4.9.2-complete.jar:$CLASSPATH"
alias antlr4='java -jar /usr/local/lib/antlr-4.9.2-complete.jar'
alias grun='java org.antlr.v4.gui.TestRig'
```
To generate python stubs:
```
antlr4 -Dlanguage=Python3 to generate python code
```
And to make the environment executable:
```
pip install antlr4-python3-runtime
```
