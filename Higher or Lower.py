import random
game = True

data = [
    {"name": "Cristiano Ronaldo", "country": "Portugal", "goals": 143},
    {"name": "Lionel Messi", "country": "Argentina", "goals": 117},
    {"name": "Ali Daei", "country": "Iran", "goals": 108},
    {"name": "Sunil Chhetri", "country": "India", "goals": 95},
    {"name": "Romelu Lukaku", "country": "Belgium", "goals": 90},
    {"name": "Mokhtar Dahari", "country": "Malaysia", "goals": 89},
    {"name": "Robert Lewandowski", "country": "Poland", "goals": 89},
    {"name": "Ali Mabkhout", "country": "UAE", "goals": 85},
    {"name": "Ferenc Puskás", "country": "Hungary", "goals": 84},
    {"name": "Godfrey Chitalu", "country": "Zambia", "goals": 79},
    {"name": "Harry Kane", "country": "England", "goals": 79},
    {"name": "Neymar", "country": "Brazil", "goals": 79},
    {"name": "Hussein Saeed", "country": "Iraq", "goals": 78},
    {"name": "Pelé", "country": "Brazil", "goals": 77},
    {"name": "Sándor Kocsis", "country": "Hungary", "goals": 75},
    {"name": "Kunishige Kamamoto", "country": "Japan", "goals": 75},
    {"name": "Bashar Abdullah", "country": "Kuwait", "goals": 75},
    {"name": "Edin Džeko", "country": "Bosnia and Herzegovina", "goals": 73},
    {"name": "Majed Abdullah", "country": "Saudi Arabia", "goals": 72},
    {"name": "Kinnah Phiri", "country": "Malawi", "goals": 71},
    {"name": "Kiatisuk Senamuang", "country": "Thailand", "goals": 71},
    {"name": "Miroslav Klose", "country": "Germany", "goals": 71},
    {"name": "Piyapong Pue-on", "country": "Thailand", "goals": 70},
    {"name": "Abdul Kadir", "country": "Indonesia", "goals": 70},
    {"name": "Stern John", "country": "Trinidad and Tobago", "goals": 70},
    {"name": "Luis Suárez", "country": "Uruguay", "goals": 69},
    {"name": "Hossam Hassan", "country": "Egypt", "goals": 69},
    {"name": "Carlos Ruiz", "country": "Guatemala", "goals": 68},
    {"name": "Robbie Keane", "country": "Republic of Ireland", "goals": 68},
    {"name": "Gerd Müller", "country": "West Germany", "goals": 68}
]

a_info = random.choice(data)
score = 0
while game:
  b_info = random.choice(data)

  while a_info == b_info:
    b_info = random.choice(data)

  print(f"Compare A: {a_info['name']}, From {a_info['country']}")
  print(f"Against B: {b_info['name']}, From {b_info['country']}")
  a = a_info['goals']
  b = b_info['goals']

  ch = input(" Type 'A' or 'B': ").upper()
  if ch == 'A':
    if a >= b:
      score += 1
      print(f"Your right! current score: {score} ")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      game = False
  else:
    if b >= a:
      score += 1
      print(f"Your right! current score: {score} ")
      a_info = b_info
    else:
      game = False
      print(f"Sorry, that's wrong. Final score: {score}")
