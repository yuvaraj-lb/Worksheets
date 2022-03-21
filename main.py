from pylatex.base_classes import Environment, CommandBase, Arguments
from pylatex.package import Package
from pylatex import Document, Section, UnsafeCommand
from pylatex.utils import NoEscape
import pandas as pd

data1 = pd.read_csv("worksheet_question_db.csv")
data = pd.DataFrame(data1)

data2 = pd.read_excel("qr_db.xlsx")
dat = pd.DataFrame(data2)

qdata1 = [i for i in dat.iloc[:,0]]

qdata2 = []

for i in range(len(qdata1)):
    ls = ["A", "B", "C"]
    for j in range(3):
        dr = ''
        dr = dr+qdata1[i]+ls[j]
        qdata2.append(dr)



class insert_img(CommandBase):
    _latex_name = 'img'
    

class insert_question(CommandBase):
    _latex_name = 'question'
    

class insert_hint(CommandBase):
    _latex_name = 'hints'


# Create a new document
def get_lib():
    
    doc.packages.append(Package('multicol'))
    doc.packages.append(Package('ragged2e'))
    doc.packages.append(Package('graphicx'))
    doc.packages.append(Package('amsmath'))
    doc.packages.append(Package('xcolor'))
    doc.packages.append(Package('geometry'))
    doc.packages.append(Package('caption'))
    doc.packages.append(Package('subcaption'))
    doc.packages.append(Package('enumitem'))
    doc.packages.append(Package('amssymb'))
    doc.packages.append(Package('multirow'))
    doc.packages.append(Package('tcolorbox'))
    doc.packages.append(Package('xparse'))

def add_custom_commands():
    
    new_comm = UnsafeCommand('newcommand', '\img', options=3,
                                extra_arguments=r'\begin{figure}[h] \centering \includegraphics[ width = #1, height = #2]{#3} \end{figure}')
    doc.append(new_comm)

    new_comm = UnsafeCommand('newcommand', '\question', options=6,
                                extra_arguments=r'\vspace{2.5mm} \begin{raggedright} \textbf{Question:} #1  #2 #3 #4 #5 #6\\ \end{raggedright}')

    doc.append(new_comm)

    new_comm = UnsafeCommand('newcommand', '\hints', options=5,
                                extra_arguments=r'\vspace{2.5mm} \begin{raggedright} #1 #2 #3 #4 #5\\ \end{raggedright} \vspace{2.5mm}')
    doc.append(new_comm)



def append_questions(qno):
    qs = data.loc[data['question_id']==qdata2[qno]]
    qslist = qs.values.flatten().tolist()
    doc.append(NoEscape(r'\question'))
    qts = qslist[2]
    doc.append(NoEscape(fr'{qts}'))
    doc.append(NoEscape(r'\hints'))
    qth = qslist[3]
    doc.append(NoEscape(fr'{qth}'))


doc = Document()
get_lib()
add_custom_commands()
for i in range(len(qdata2)):
    append_questions(i)
doc.generate_pdf('with_img', clean_tex=False, compiler='pdflatex')
