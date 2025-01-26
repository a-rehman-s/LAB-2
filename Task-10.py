import os

package = input("Enter package name to install: ")
os.system(f"pip install {package}")
