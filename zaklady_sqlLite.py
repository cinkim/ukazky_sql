################################################
### Ukoly a poznamky k prednasce o SQL - PyLadies Plzen 16.2.2021 online (video dovysvetleni)
### author: Jana Koukalova 
### description: zaklady o SQL jazyku na demu https://www.sqlitetutorial.net
### source: https://github.com/koukalka/ukazky_sql/blob/main/zaklady_sqlLite.py


# SQL extensions: https://marketplace.visualstudio.com/items?itemName=leo-buneev.vscode-sql-template-literal-js-ts-vue
# https://www.sqlitetutorial.net/tryit/query/sqlite-select/#5

#TO DO - priklady na SQL:

######################### SELECT - customers:
# dotazovani vysledku, videt je

# Vyber zákazníky, které jsou z České republiky
SELECT * FROM customers WHERE Country = "Czech Republic";
# * - říká všechno, jinak jména sloupečků

# Vyber zákazníky, které se jmenuji Frank/Mark
SELECT * FROM customers WHERE FirstName = "Mark" OR FirstName = "Mark";

# Vyber zákazníky, kteří pracují v Applu
SELECT * FROM customers WHERE Company LIKE "%Apple%"
# % nahrazuje žádný až nekonečno znaků - před znamená cokoliv předem nebo nic, za cokoliv za slovem a nebo nic

# Vyber zákazníky, kteří pracují v Applu nebo Microsoftu
SELECT * FROM customers WHERE Company LIKE "%Apple%" OR Company LIKE "Micro%";

# Vypiš všechny jména zákazníků bez opakování
SELECT DISTINCT FirstName FROM customers;
# DISTINCT - neopakuj mi tam záznam (vše jen jednou)

# Vypiš všechny křestní jména seřazená od A do Z
SELECT DISTINCT FirstName FROM customers
ORDER BY FirstName ASC #defaultne, ascending ... od A do Z, 1-100

SELECT DISTINCT FirstName FROM customers
ORDER BY FirstName DESC # descending ... od Z do A, 100 - 1

# COUNT
# počet záznamů v dané tabulce 
SELECT COUNT(*) FROM employees
SELECT COUNT(*) FROM customers

# Vypiš kolik zákazníků jsou z Německa
SELECT COUNT(*) FROM customers WHERE country = "Germany"

# Vypis kolik zákazníků pracují v Applu
SELECT COUNT(*) AS pocet_zakazniku FROM customers WHERE company LIKE "App%"

#Vypiš kolikrát se opakují daná křestní jména
SELECT FirstName, COUNT(*) FROM customers
GROUP BY 1 
# GROUP BY pro agregační funkce - min, max, počet, průměr, apod. - musí být! jinak dělá něco jiného
# muzete videt i cisla - tj 1 znamena prvni sloupecek, ktery v dotazu pisu

#Vypiš kolikrát se opakují daná křestní jména seřazená od A do Z
SELECT FirstName, COUNT(*) FROM customers
GROUP BY 1
ORDER BY 1

#Vypiš kolikrát se opakují daná křestní jména seřazená podle největšího výskytu - chci zjistit, kteří zákazníci mají nejčastější jména
SELECT FirstName, COUNT(*) AS pocet_jmen FROM customers
GROUP BY 1
ORDER BY pocet_jmen


####################### vytvoreni tabulky a prace s ni
# https://www.sqlitetutorial.net/tryit/query/sqlite-create-table/#1
# vytvorit tabulku CREATE TABLE
# naplnit INSERT
# podivat se na ni SELECT
# updatovat zaznam UPDATE
# smazat tabulku - DROP celou pryc, DELETE - ponecha strukturu

#Vytvor tabulku zamestnancu, id je primarni klic
CREATE TABLE zamestnanci (
	id_zam integer PRIMARY KEY,
	jmeno_zam NVARCHAR(50) NOT NULL,
	prijmeni_zam text NOT NULL
);

#Vytvor tabulku zakazniku s vazbou na tabuku zamestnancu
# budu tedy videt, kdo se stara o jake zakazniky - foreign key (cizi klic odkazuje se na jinu tabulku)
CREATE TABLE zakaznici (
	id_zak integer PRIMARY KEY,
	jmeno_zak NVARCHAR(50) NOT NULL,
	prijmeni_zak text NOT NULL,
  id_zam integer, --nejrpve si klic vytvorim
   FOREIGN KEY(id_zam) REFERENCES zamestnanci(id_zam) -- a pak reknu vazbu neboli referenci na tabuku a sloupecek na co chci odkazovat
);

#Vloz do nich zaznamy
INSERT INTO zamestnanci -- pokud chci vlozit zaznamy do vsech sloupecku, nemusim je vypisovat
VALUES(1, "Pepa","Novak");
INSERT INTO zamestnanci
VALUES(2, "Pepa","Koukal");

INSERT INTO zakaznici
VALUES(1, "Jana","Koukalova", "1");
INSERT INTO zakaznici
VALUES(2, "Milena","Novakova", NULL);
INSERT INTO zakaznici
VALUES(3, "Petra","Svobodova", "2");

#Podivej se na to, co si vytvořil(a)
Select * from zakaznici;
SELECT * FROM zamestnanci;

# Zmen jmeno u zamestnance cislo 2 na Petr  a zkontroluj
UPDATE zamestnanci SET jmeno_zam = "Petr"
WHERE id_zam = 2

# Smaz tabulku - jenom data
DELETE FROM zakaznici; 
# jde potom vkladat zaznamy, struktura ponechana

# Smaz tabulkou - cela fuc
DROP TABLE zakaznici;
# nejde potom vkladat zaznamy, tabulka je fuc

############################## JOIN spojeni dvou tabulek
## POTREBUJI MIT DVE TABULKY S PRIMARNIMI A CIZIMI KLICI vytvorene!!!

## JOIN, INNER JOIN - jen to, co maji obe dve tabulky spolecneho
SELECT
	id_zak,
	jmeno_zak,
	cust.id_zam AS id_zam, --!! alias, zde je NUTNY nebot existuji dva sloupecky se stejnym nazvem 
  --proto musim vybrat, jaky sloupec (zda z tabulky zamestnanci nebo zakaznici) chci vybrat
	jmeno_zam
FROM
	zakaznici cust --alias pro zakaznici je cust
INNER JOIN zamestnanci empl -- alias pro zamestnance je empl
ON cust.id_zam = empl.id_zam;
-- mam jen 2 vysledky

### LEFT RIGHT JOIN - vysledek je cela tabulka vlevo ci vpravo a napojene informace
SELECT
	id_zak,
	jmeno_zak,
	cust.id_zam AS id_zam, --alias
	jmeno_zam
FROM
	zakaznici cust
LEFT JOIN zamestnanci empl
ON cust.id_zam = empl.id_zam;
-- zde 3 vysledky

############################## 
## Pozn: dalsi a slozitejsi prikazy ROW NUMBER, regulární výrazy, OVER PARTITON BY a dalsi window funkce - nekdy priste ;)
## Vice info o nas dvou: https://www.lenk.solutions/ https://www.skoukalkou.online/
