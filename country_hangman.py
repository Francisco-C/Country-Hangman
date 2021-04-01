import random
import re

listOfCountries = [
"TUNISIA",
"REPUBLIC OF CONGO",
"ALBANIA",
"PALESTINE",
"LIBYA",
"GABON",
"UKRAINE",
"INDIA",
"MAURITANIA",
"MOROCCO",
"AFGHANISTAN",
"SWEDEN",
"LESOTHO",
"URUGUAY",
"CYPRUS",
"TANZANIA",
"SLOVAKIA",
"ISRAEL",
"CROATIA",
"AUSTRIA",
"SOUTH AFRICA",
"DJIBOUTI",
"MONTENEGRO",
"FIJI",
"TAIWAN",
"KYRGYZSTAN",
"MYANMAR",
"KENYA",
"SAUDI ARABIA",
"MAURITIUS",
"SOMALIA",
"KIRIBATI",
"MONACO",
"QATAR",
"TIMOR-LESTE",
"KAZAKHSTAN",
"SRI LANKA",
"ANDORRA",
"SINGAPORE",
"NIGER",
"GREECE",
"IVORY COAST",
"BHUTAN",
"ECUADOR",
"PALAU",
"MARSHALL ISLANDS",
"THAILAND",
"MOLDOVA",
"LUXEMBOURG",
"CZECHIA",
"GUYANA",
"JAPAN",
"GUINEA-BISSAU",
"BULGARIA",
"ICELAND",
"JORDAN",
"NIGERIA",
"DOMINICAN REPUBLIC",
"NICARAGUA",
"HUNGARY",
"SAMOA",
"LIBERIA",
"EL SALVADOR",
"PARAGUAY",
"IRAN",
"AZERBAIJAN",
"ZAMBIA",
"FRANCE",
"MICRONESIA",
"ARMENIA",
"ERITREA",
"AUSTRALIA",
"UNITED KINGDOM",
"VATICAN CITY",
"CAMEROON",
"BRAZIL",
"EGYPT",
"CUBA",
"COSTA RICA",
"SIERRA LEONE",
"BOSNIA HERZEGOVINA",
"UZBEKISTAN",
"ITALY",
"IRELAND",
"GUINEA",
"EQUATORIAL GUINEA",
"LITHUANIA",
"UNITED STATES",
"LAOS",
"VENEZUELA",
"CHAD",
"YEMEN",
"COMOROS",
"SEYCHELLES",
"SAN MARINO",
"SOUTH SUDAN",
"POLAND",
"NORTH KOREA",
"SURINAME",
"SÃO TOMÉ AND PRÍNCIPE",
"ROMANIA",
"ESTONIA",
"BOTSWANA",
"MALI",
"BURUNDI",
"TURKMENISTAN",
"UGANDA",
"KOSOVO",
"ZIMBABWE",
"CHINA",
"KUWAIT",
"ETHIOPIA",
"BENIN",
"BELARUS",
"MALTA",
"CANADA",
"NAMIBIA",
"JAMAICA",
"SAINT VINCENT AND THE GRENADINES",
"SUDAN",
"SERBIA",
"BOLIVIA",
"PAPUA NEW GUINEA",
"VANUATU",
"LATVIA",
"BRUNEI",
"OMAN",
"ARGENTINA",
"NETHERLANDS",
"NAURU",
"HAITI",
"SPAIN",
"GUATEMALA",
"MALDIVES",
"BANGLADESH",
"LIECHTENSTEIN",
"NEPAL",
"SOUTH KOREA",
"SOLOMON ISLANDS",
"FINLAND",
"NEW ZEALAND",
"PORTUGAL",
"MALAYSIA",
"MONGOLIA",
"CAPE VERDE",
"ALGERIA",
"PHILIPPINES",
"GEORGIA",
"GHANA",
"SAINT KITTS AND NEVIS",
"SENEGAL",
"MEXICO",
"ANGOLA",
"CENTRAL AFRICAN REPUBLIC",
"SLOVENIA",
"TUVALU",
"HONDURAS",
"BARBADOS",
"CHILE",
"TONGA",
"BURKINA FASO",
"GRENADA",
"RUSSIA",
"TOGO",
"NORTH MACEDONIA",
"SYRIA",
"MOZAMBIQUE",
"DOMINICA",
"MALAWI",
"CAMBODIA",
"DENMARK",
"BAHRAIN",
"THE GAMBIA",
"PANAMA",
"TRINIDAD AND TOBAGO",
"UNITED ARAB EMIRATES",
"SAINT LUCIA",
"MADAGASCAR",
"GERMANY",
"PAKISTAN",
"PERU",
"BAHAMAS",
"TAJIKISTAN",
"COLOMBIA",
"LEBANON",
"BELIZE",
"ANTIGUA AND BARBUDA",
"IRAQ",
"INDONESIA",
"DEMOCRATIC REPUBLIC OF THE CONGO",
"RWANDA",
"NORWAY",
"VIETNAM",
"TURKEY",
"BELGIUM",
"ESWATINI",
"SWITZERLAND"]

listOfLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lettersUsed = ""

randomCountry = random.choice(listOfCountries)

lives = 6
wonTheGame = False

print("Country Hangman \n")

countryEncrypted = re.sub("[A-Z]", "_ ", randomCountry)
print("Country: ", countryEncrypted, "\n")

while lives > 0 and wonTheGame == False:

	print("Lives left: ", lives, "\n")
	print("Letters Available: ")
	print(listOfLetters, "\n")

	playerInput = input("Provide a valid letter or the answer: ")
	playerInput2 = playerInput.upper()

	while len(playerInput2) == 1 and playerInput2 not in listOfLetters:

		print("Invalid letter provided!")
		playerInput = input("Provide a valid letter or the answer: ")
		playerInput2 = playerInput.upper()

	if playerInput2 in listOfLetters:

		listOfLetters.remove(playerInput2)

		if playerInput2 not in randomCountry:
			print("The country does not contain that letter!")
			print("1 life lost! \n")
			lives -= 1
			lettersUsed += playerInput2
			countryEncrypted = re.sub("(?:(?![" + re.escape(lettersUsed) + "])[A-Z])", "_ ", randomCountry)
			print("Country: ", countryEncrypted, "\n")
		else:
			print("\nYou found a letter!")
			lettersUsed += playerInput2
			countryEncrypted = re.sub("(?:(?![" + re.escape(lettersUsed) + "])[A-Z])", "_ ", randomCountry)
			print("Country: ", countryEncrypted, "\n")
	else:
		if playerInput2 == randomCountry:
			print("Congratulations you won the game!")
			print("Country: ", randomCountry)
			wonTheGame = True
		else:
			print("That is not the correct answer!")
			print("1 life lost! \n")
			lives -= 1
			if lives > 0:
				if lettersUsed != "":
					countryEncrypted = re.sub("(?:(?![" + re.escape(lettersUsed) + "])[A-Z])", "_ ", randomCountry)
					print("Country: ", countryEncrypted, "\n")
				else:
					countryEncrypted = re.sub("[A-Z]", "_ ", randomCountry)
					print("Country: ", countryEncrypted, "\n")

if lives == 0:
	print("Lives left: ", lives)
	print("The correct answer was: ", randomCountry)
	print("GAME OVER")