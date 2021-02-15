# Created with Pyto
import sqlite3

from sqlite3 import Error

# SQL kod pro vytvoreni tabulky s projekty
sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

# SQL kod pro vytvoreni tabulky s ukoly
sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""
# funkce pro vytvoreni noveho zaznamu v tabulce s projekty
def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

# funkce pro vytvoreni noveho zaznamu v tabulce s ukoly
def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

# vytvorim si spojeni na soubor s databazi
# pokud soubor neexistuje, vytvori se
conn = sqlite3.connect("test.db")

# vytvorim si ktery mi umozni pracovat s daty
c = conn.cursor()

# spustim SQL prikaz na vytvoreni tabulky s projekty
c.execute(sql_create_projects_table)

# spustim SQL prikaz na vytvoreni tabulky s ukoly
c.execute(sql_create_tasks_table)

# smazu si vsechny zaznamy v tabulce s projekty a ukoly
# !! zakomentuj nasledujici 2 radky a kazdym spustenim skriptu ti budou pribyvat zaznamy
c.execute("DELETE FROM projects")
c.execute("DELETE FROM tasks")

# definice noveho projektu
project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');

# vlozeni projektu do DB pomoci pripravene funkce a ziskani jeho ID pro provazani s ukolem
project_id = create_project(conn, project)

# definice novych ukolu a provazani jej s projektem ktery jsme pred chvili vytvorili
task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

# vlozeni ukolu do DB pomoci pripravene funkce
create_task(conn, task_1)
create_task(conn, task_2)

# zavolani SQL pro vypis vsech ukolu
# nyni se pripravi vysledek uvnitr sqlite
c.execute("SELECT * FROM tasks")

# natazeni vsech radku vysledku do pythonu
rows = c.fetchall()

# print vysledku
for row in rows:
    print(row)

