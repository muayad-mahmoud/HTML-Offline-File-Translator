from bs4 import BeautifulSoup
import re
from googletrans import Translator
from googletrans import LANGUAGES
import os
import time
from deep_translator import GoogleTranslator
import threading
from datetime import datetime


def recursiveSolution(elements):
    if len(elements) == 0:
        return False

    for each in elements:
        now = datetime.now()
        print(now.strftime("%m/%d/%Y %H:%M:%S"), end="", flush=True),
        print("\r", end="", flush=True),
        if each.text is None:
            continue
        if each.string is None:
            text = [c.strip()
                    for c in each if c.name is None and c.strip() != ""]
            if text:
                translated_text = None
                for i in range(len(text)):
                    if text[i] is None:
                        continue
                    else:
                        # print(text[i])

                        try:
                            translated_text = translator.translate(
                                text=text[i])
                        except:
                            pass
                        if translated_text is not None:
                            for x in range(len(each.contents)):
                                if str(text[i]) in each.contents[x]:
                                    replacedstr = str(each.contents[x]).replace(
                                        str(text[i]), str(translated_text))
                                    if "None" in replacedstr:
                                        replacedstr = replacedstr.replace(
                                            "None", "")
                                    each.contents[x].replaceWith(replacedstr)
                                    # print("replaced advanced " +
                                    # str(text[i]) + str(translated_text))
                        else:
                            pass

                # print(each.contents)

            children = each.findChildren(
                ['div', 'caption', 'ul', 'td', 'em', 'li', 'b', 'a', 'h1', 'h2', 'h3', 'p', 'strong', 'button', 'span', 'i'])
            recursiveSolution(children)
        if each.string:
            try:

                text = each.text.strip()

                translated_text = translator.translate(text=each.text.strip())

                each.string.replace_with(translated_text)
                # print(each.text)
            except:
                pass

    return


''''''''''''''''
def loopOverItems(elements):
    for child in elements:
        text = child.text.strip()

        translated_text = translator.translate(
        child.text.strip(), src="en", dest="hi")

        child.string.replace_with(translated_text.text)
        print(child.text)

def translate(child_element):
    text = child_element.text.strip()

    translated_text = translator.translate(
    child_element.text.strip(), src="en", dest="hi")

    child_element.string.replace_with(translated_text.text)
    print(child_element.text)
for each in elements:
    if each.text is None:
        pass
    else:
        if each.string is None:

            children = each.findChildren(
                ['a', 'h1', 'h2', 'h3', 'p', 'strong', 'button', 'span', 'i'])
            for child in children:
                if child.string is None:
                    pass
                else:
                    translate(child_element=child)
        else:

            text = each.text.strip()

            translated_text = translator.translate(
                each.text.strip(), src="en", dest="hi")

            each.string.replace_with(translated_text.text)
            print(each.text)
'''''''''''


'''''''''''''''''''''
url = "C:\\Users\\Helliuminati\\Desktop\\PyAssign\\index.html"
page = open(url, encoding="utf8")

soup = BeautifulSoup(page.read())

elements = soup.find_all(
    ['a', 'h1', 'h2', 'h3', 'p', 'strong', 'button', 'span', 'i'])
translator = GoogleTranslator(source='en', target='hi')
recursiveSolution(elements=elements)

with open("example_modified.html", "wb") as f_output:
    f_output.write(soup.prettify("utf-8"))
'''''''''''
##Change Directory and it will scan the directory for files
directory = ""
done_files = []
os.chdir(directory)
try:
    with open('log.txt') as fp:
        temp_list = fp.readlines()
        done_files = [x.strip() for x in temp_list]
    fp.close()
except:
    pass
count = 0
for (dir_path, dir_name, files) in os.walk(directory, topdown=False):

    for filename in files:
        if filename.endswith('.html') and str(os.path.join(dir_path, filename)) not in done_files:
            count = count + 1

print(f"Excpected Number of files is: {count}")

# print(done_files)
for (dir_path, dir_name, files) in os.walk(directory, topdown=False):
    failed = False

    for filename in files:

        # print(os.path.join(dir_path, filename))
        if filename.endswith('.html') and str(os.path.join(dir_path, filename)) not in done_files:
            try:
                url = os.path.join(dir_path, filename)
                # print(url)
                print("Starting filename: " + url)
                page = open(url, encoding="utf8")
                soup = BeautifulSoup(page.read(), features="html.parser")
            except:
                print("Skipping File")
                failed = True
                continue
            if failed:
                continue
            else:
                now = datetime.now()

                elements = soup.find_all(
                    ['caption', 'ul', 'td', 'em', 'li', 'b', 'a', 'h1', 'h2', 'h3', 'p', 'strong', 'button', 'span', 'i'])
                translator = GoogleTranslator(source='en', target='hi')
                recursiveSolution(elements=elements)
                with open(url, "wb") as f_output:
                    f_output.write(soup.prettify("utf-8"))
                print("DONE")
                done_files.append(os.path.join(dir_path, filename))
                with open('log.txt', 'w') as fp:
                    fp.write('\n'.join(str(item) for item in done_files))
                fp.close
                diff = (datetime.now() - now).total_seconds()
                print(f"Time Taken: {diff} seconds")
                count = count - 1
                print(f"Files Remaining: {count}")

        else:
            continue
