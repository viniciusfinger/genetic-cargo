import webbrowser
import shutil
import pathlib
import os


path = str(pathlib.Path().resolve())

def file_exists(file_name):
    path = str(pathlib.Path().resolve())+"/web/"+file_name
    file = pathlib.Path(path)

    return pathlib.Path.exists(file)


def move_table():
    shutil.move(path+"/tabela.html",path+"/web")
    shutil.move(path+"/tabela_valortotal.html",path+"/web")
    shutil.move(path+"/tabelaConfiguracoes.html",path+"/web")

def delete_old_tables():
    if file_exists("tabela.html"):
        os.remove(path+"/web/tabela.html")

    if file_exists("tabela_valortotal.html"):
        os.remove(path+"/web/tabela_valortotal.html")

    if file_exists("tabelaConfiguracoes.html"):
        os.remove(path+"/web/tabelaConfiguracoes.html")

def open_dashboard():
    delete_old_tables()
    move_table()
    webbrowser.open(path+"/web/lista.html",new=1)
