from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as ec
import tkinter as tk
from tkinter import * 
from tkinter.filedialog import askopenfilename
from tkinter import messagebox 
import time
import pathlib
import speech_recognition as sr
import ffmpy
import requests
import urllib
from pydub import AudioSegment
import os

class My_App(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(str(pathlib.Path(__file__).parent.absolute()) + '\\chromedriver.exe',options=options)
        url="https://quillbot.com/"
        self.driver.get(url)
        elelogins = self.driver.find_elements_by_class_name('MuiButton-label')
        for i in range(0, len(elelogins)):
            if (elelogins[i].text == "Log In"):
                elelogins[i].click()
                break

        time.sleep(2)

        eleInputs = self.driver.find_elements_by_class_name('MuiFilledInput-input')
        eleInputs[0].send_keys('fadeevdoma@gmail.com')
        eleInputs[1].send_keys('quillbotpass')

        self.driver.find_element_by_class_name('auth-btn').click()        
        
        lblInput = Label(self.parent, font="Verdana 10 bold", text = "InputText : ")
        lblInput.place(x=70, y=40)
        
        self.txtInput = tk.Text(root, font=('calibre',10,'normal'), height=8, width=50) 
        self.txtInput.pack()
        self.txtInput.place(x=170, y=40)		

        lblOutput = Label(self.parent, font="Verdana 10 bold", text = "OutputText : ")
        lblOutput.place(x=70, y=200)

        self.txtOutput = tk.Text(root, font=('calibre',10,'normal'), height=8, width=50) 
        self.txtOutput.pack()
        self.txtOutput.place(x=170, y=200)			

        self.btnStart = tk.Button(self.parent, text="Start", command = self.OnStart, width=12)
        self.btnStart.pack()
        self.btnStart.place(x=400, y=350)

    def OnStart(self):        
        if self.txtInput.get("1.0", 'end-1c') == "":
            messagebox.showwarning("Warning", "Please input text to rewrite!") 

        sInput = self.txtInput.get("1.0", 'end-1c')
        sListInput = sInput.split('\n')
        sListOutput = sListInput       

        try: 
            if(len(self.driver.find_elements_by_class_name('MuiDialog-paper')) > 0):
                elebuttons = self.driver.find_elements_by_class_name('MuiIconButton-root')
                for i in range(0, len(elebuttons)):
                    try:
                        elebuttons[i].click()
                        break
                    except:
                        pass     

            eleSliders = self.driver.find_elements_by_class_name('MuiSlider-thumbColorPrimary')

            for i in range(0, len(eleSliders)):
                try:
                    eleSliders[i].send_keys(Keys.ARROW_RIGHT)
                    eleSliders[i].send_keys(Keys.ARROW_RIGHT)
                    eleSliders[i].send_keys(Keys.ARROW_RIGHT)
                    break
                except:
                    pass

            for v in range(0, len(sListInput)):

                if (sListInput[v] != ""):

                    if(len(self.driver.find_elements_by_class_name('MuiDialog-paper')) > 0):
                        elebuttons = self.driver.find_elements_by_class_name('MuiIconButton-root')
                        for i in range(0, len(elebuttons)):
                            try:
                                elebuttons[i].click()
                                break
                            except:
                                pass     

                    WebDriverWait(self.driver, 600).until(ec.element_to_be_clickable((By.CLASS_NAME, 'QuillButton-sc-12j9igu-0')))              

                    eleInputbox = self.driver.find_element_by_id('inputText')
                    eleInputbox.clear()
                    eleInputbox.send_keys(sListInput[v])                

                    time.sleep(1)
                    WebDriverWait(self.driver, 600).until(ec.element_to_be_clickable((By.CLASS_NAME, 'QuillButton-sc-12j9igu-0'))).click()
                    time.sleep(1)

                    WebDriverWait(self.driver, 600).until(ec.element_to_be_clickable((By.CLASS_NAME, 'QuillButton-sc-12j9igu-0')))

                    sOutput = self.driver.find_element_by_id('articleTextArea').text
                    sListOutput[v] = sOutput

        except Exception as e:
            messagebox.showwarning("Warning", str(e))
            
        self.txtOutput.delete('1.0', 'end-1c')
        self.txtOutput.insert('1.0', '\n'.join(sListOutput))

root = tk.Tk(className=' Quillbot Rewriter')
root.geometry("600x390")
root.resizable(False, False) 
My_App(root)
root.mainloop()