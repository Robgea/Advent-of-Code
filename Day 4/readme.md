##DAY 4##

#First Problem#

A batchfile is generated with sequential groupings of text, each of which has these potential fields:

* byr (Birth Year)
* iyr (Issue Year)
* eyr (Expiration Year)
* hgt (Height)
* hcl (Hair Color)
* ecl (Eye Color)
* pid (Passport ID)
* cid (Country ID)

The goal for the first problem is to check that every passport has all fields, or that it's only missing "cid".

(My solution produced the answer minus one.)

#Second Problem#

Involves taking the dataset from the first and validating the data.

* byr (Birth Year) - four digits; at least 1920 and at most 2002.
* iyr (Issue Year) - four digits; at least 2010 and at most 2020.
* eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
* hgt (Height) - a number followed by either cm or in:
* If cm, the number must be at least 150 and at most 193.
* If in, the number must be at least 59 and at most 76.
* hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
* ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
* pid (Passport ID) - a nine-digit number, including leading zeroes.

(My solution produced the correct answer plus one.)