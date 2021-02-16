# extensions: https://marketplace.visualstudio.com/items?itemName=leo-buneev.vscode-sql-template-literal-js-ts-vue
# SQLite

# dotazy mi funguji
# https://www.sqlitetutorial.net/tryit/query/sqlite-select/#5

#TO DO - priklady na SQL:

SELECT - employees:
# Vyber zákazníky, které jsou z České republiky
# Vyber zákazníky, které se jmenuji Frank/Mark
# Vyber zákazníky, kteří pracují v Applu
# Vyber zákazníky, kteří pracují v Applu nebo Microsoftu
# Vypiš všechny jména zákazníků bez opakování
# Vypiš všechny křestní jména seřazená od A do Z

SELECT * FROM customers where Company = "Microsoft Corporation"
SELECT * FROM customers where Company = "Microsoft Corporation" or Company = "Apple Inc."
SELECT DISTINCT FirstName FROM customers

# COUNT
#Vypiš kolikrát se opakují daná křestní jména (seřazená od největšího po nejmenší)
SELECT FirstName, COUNT(*) as cnt FROM customers group by 1 order by cnt desc;

SELECT COUNT(*) FROM customers
WHERE COUNTRY = 'Canada';

SELECT * FROM customers
WHERE COUNTRY = 'Canada';

# https://www.sqlitetutorial.net/tryit/query/sqlite-create-table/#1
# vytvorit tabulku
# naplnit
# podivat se na ni
# updatovat zaznam
# smazat tabulku - DROP celou pryc, DELETE - ponecha strukturu

